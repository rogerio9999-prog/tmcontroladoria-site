#!/usr/bin/env python3
"""
Gerador do site + blog da TM Controladoria.

Uso:
    python build.py              gera o site em _site/
    python build.py --serve      gera e abre um servidor local em http://localhost:8000
    python build.py --rascunhos  inclui posts marcados como rascunho e com data futura

Os posts ficam em posts/*.md. Veja CLAUDE.md para o formato e o guia editorial.
"""
from __future__ import annotations

import html
import json
import os
import re
import shutil
import sys
import unicodedata
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

try:
    import markdown
except ImportError:
    sys.exit("Falta a biblioteca 'markdown'. Rode: python -m pip install -r requirements.txt")

ROOT = Path(__file__).resolve().parent
POSTS_DIR = ROOT / "posts"
OUT = ROOT / "_site"
STATIC_FILES = ["index.html", "parceiros.html", "styles.css", "blog.css"]

SITE_URL = "https://tmcontroladoria.com.br"
SITE_NAME = "TM Controladoria e Soluções Contábeis"
WHATSAPP = "https://wa.me/553433253919"
POSTS_PER_PAGE = 12
BRT = timezone(timedelta(hours=-3))

# Ícones e imagem de compartilhamento (WhatsApp, LinkedIn, Facebook, Google). Ficam em assets/.
OG_IMAGE = SITE_URL + "/assets/og-image.png"
HEAD_EXTRA = f"""<meta property="og:image" content="{OG_IMAGE}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="TM Controladoria e Soluções Contábeis">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" href="/assets/icon-512.png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">"""

CATEGORIES = {
    "Reforma Tributária": "reforma-tributaria",
    "Simples Nacional": "simples-nacional",
    "MEI": "mei",
    "Prazos e Agenda": "prazos",
    "Pessoa Física": "pessoa-fisica",
    "Trabalhista e Folha": "trabalhista",
    "Gestão e Controladoria": "gestao",
}
REQUIRED = ["titulo", "resumo", "data", "categoria", "fontes"]
MESES = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho",
         "agosto", "setembro", "outubro", "novembro", "dezembro"]


# --------------------------------------------------------------------------- #
# Modelo e leitura dos posts
# --------------------------------------------------------------------------- #
@dataclass
class Post:
    slug: str
    titulo: str
    resumo: str
    data: date
    categoria: str
    fontes: list[str]
    html: str
    palavras: int
    atualizado: date | None = None
    tags: list[str] = field(default_factory=list)
    autor: str = "Equipe TM Controladoria"
    rascunho: bool = False

    @property
    def url(self) -> str:
        return f"/blog/{self.slug}/"

    @property
    def cat_slug(self) -> str:
        return CATEGORIES[self.categoria]

    @property
    def leitura(self) -> int:
        return max(1, round(self.palavras / 200))


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def parse_front_matter(raw: str, path: Path) -> tuple[dict, str]:
    """Front matter simples: 'chave: valor' e listas com '  - item'."""
    if not raw.startswith("---"):
        raise ValueError(f"{path.name}: o arquivo precisa começar com '---'")
    _, fm, body = raw.split("---", 2)
    meta: dict = {}
    key = None
    for line in fm.strip().splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        m = re.match(r"^\s+-\s+(.*)$", line)
        if m and key:
            meta.setdefault(key, [])
            if not isinstance(meta[key], list):
                raise ValueError(f"{path.name}: '{key}' mistura valor e lista")
            meta[key].append(unquote(m.group(1)))
            continue
        m = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if not m:
            raise ValueError(f"{path.name}: linha inválida no cabeçalho: {line!r}")
        key, value = m.group(1), m.group(2).strip()
        if value.startswith("[") and value.endswith("]"):
            meta[key] = [unquote(v) for v in value[1:-1].split(",") if v.strip()]
        elif value:
            meta[key] = unquote(value)
    return meta, body


def unquote(v: str) -> str:
    v = v.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        return v[1:-1]
    return v


def parse_date(v: str, path: Path, campo: str) -> date:
    try:
        return date.fromisoformat(v)
    except ValueError:
        raise ValueError(f"{path.name}: '{campo}' deve estar no formato AAAA-MM-DD (recebi {v!r})")


def render_markdown(body: str) -> str:
    md = markdown.Markdown(
        extensions=["extra", "sane_lists", "toc"],
        extension_configs={"toc": {"slugify": lambda v, sep: slugify(v), "permalink": False}},
    )
    out = md.convert(body)
    # links externos abrem em nova aba
    out = re.sub(r'<a href="(https?://[^"]+)"', r'<a href="\1" target="_blank" rel="noopener"', out)
    # tabelas roláveis no celular
    out = out.replace("<table>", '<div class="table-wrap"><table>').replace("</table>", "</table></div>")
    return out


def load_posts(incluir_rascunhos: bool) -> list[Post]:
    hoje = datetime.now(BRT).date()
    posts, slugs, erros = [], set(), []
    for path in sorted(POSTS_DIR.glob("*.md")):
        try:
            raw = path.read_text(encoding="utf-8")
            linhas = [str(i) for i, l in enumerate(raw.splitlines(), 1) if "—" in l or "–" in l]
            if linhas:
                raise ValueError(f"{path.name}: travessão (— ou –) nas linhas {', '.join(linhas)}. "
                                 "Reescreva com vírgula, dois-pontos, parênteses ou ponto final.")
            meta, body = parse_front_matter(raw, path)
            faltando = [k for k in REQUIRED if not meta.get(k)]
            if faltando:
                raise ValueError(f"{path.name}: faltam os campos {', '.join(faltando)}")
            if meta["categoria"] not in CATEGORIES:
                raise ValueError(f"{path.name}: categoria '{meta['categoria']}' não existe. "
                                 f"Use uma de: {', '.join(CATEGORIES)}")
            if not isinstance(meta["fontes"], list):
                meta["fontes"] = [meta["fontes"]]
            slug = meta.get("slug") or re.sub(r"^\d{4}-\d{2}-\d{2}-", "", path.stem)
            slug = slugify(slug)
            if slug in slugs:
                raise ValueError(f"{path.name}: slug '{slug}' repetido")
            slugs.add(slug)
            post = Post(
                slug=slug,
                titulo=meta["titulo"],
                resumo=meta["resumo"],
                data=parse_date(meta["data"], path, "data"),
                atualizado=parse_date(meta["atualizado"], path, "atualizado") if meta.get("atualizado") else None,
                categoria=meta["categoria"],
                fontes=meta["fontes"],
                tags=meta.get("tags", []) if isinstance(meta.get("tags", []), list) else [meta["tags"]],
                autor=meta.get("autor", "Equipe TM Controladoria"),
                rascunho=str(meta.get("rascunho", "false")).lower() in ("true", "sim", "1"),
                html=render_markdown(body),
                palavras=len(re.findall(r"\w+", body)),
            )
        except ValueError as e:
            erros.append(str(e))
            continue
        if not incluir_rascunhos and (post.rascunho or post.data > hoje):
            continue
        posts.append(post)
    if erros:
        sys.exit("Erros nos posts:\n  - " + "\n  - ".join(erros))
    posts.sort(key=lambda p: (p.data, p.slug), reverse=True)
    return posts


# --------------------------------------------------------------------------- #
# Templates
# --------------------------------------------------------------------------- #
e = html.escape


def data_br(d: date) -> str:
    return f"{d.day} de {MESES[d.month - 1]} de {d.year}"


def data_curta(d: date) -> str:
    return f"{d.day:02d} {MESES[d.month - 1][:3]} {d.year}"


def header() -> str:
    return f"""<header class="site-header">
  <div class="wrap nav">
    <a class="brand" href="/" aria-label="{SITE_NAME}"><span class="brand-mark">TM<span>.</span></span><span class="brand-name">Controladoria e<br>Soluções Contábeis</span></a>
    <button class="nav-toggle" id="navToggle" aria-label="Abrir menu" aria-expanded="false">☰</button>
    <ul class="nav-links" id="navLinks">
      <li><a href="/#servicos">Serviços</a></li>
      <li><a href="/#reforma">Reforma Tributária</a></li>
      <li><a href="/#pessoa-fisica">Pessoa Física</a></li>
      <li><a href="/blog/" class="is-active">Blog</a></li>
      <li><a href="/parceiros.html">Parceiros</a></li>
      <li class="nav-only-mobile"><a href="/#contato">Contato</a></li>
      <li class="nav-only-mobile nav-menu-cta"><a class="btn btn--gold" href="{WHATSAPP}" target="_blank" rel="noopener">Falar no WhatsApp</a></li>
    </ul>
    <div class="nav-cta">
      <a class="btn btn--ghost" href="/#contato">Contato</a>
      <a class="btn btn--gold" href="{WHATSAPP}" target="_blank" rel="noopener">Fale conosco</a>
    </div>
  </div>
</header>"""


def footer() -> str:
    cats = "\n".join(f'          <li><a href="/blog/categoria/{s}/">{e(c)}</a></li>' for c, s in CATEGORIES.items())
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <a class="brand brand--footer" href="/" aria-label="{SITE_NAME}"><span class="brand-mark">TM<span>.</span></span><span class="brand-name">Controladoria e<br>Soluções Contábeis</span></a>
        <p style="margin-top:14px;max-width:38ch">TM Controladoria e Soluções Contábeis LTDA. Contabilidade, controladoria e assessoria tributária para empresas e pessoas físicas.</p>
        <p style="font-size:.85rem"><a href="/feed.xml">Assine o feed RSS do blog</a></p>
      </div>
      <div>
        <h4>Blog</h4>
        <ul>
{cats}
        </ul>
      </div>
      <div>
        <h4>Contato</h4>
        <ul>
          <li><a href="{WHATSAPP}" target="_blank" rel="noopener">(34) 3325-3919</a></li>
          <li><a href="mailto:contabilidade@tmcontroladoria.com.br">contabilidade@tmcontroladoria.com.br</a></li>
          <li>Praça Rui Barbosa, 300, Sala 30<br>Uberaba/MG, CEP 38010-240</li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© {datetime.now(BRT).year} TM Controladoria e Soluções Contábeis LTDA. Todos os direitos reservados.</span>
      <span>tmcontroladoria.com.br</span>
    </div>
  </div>
</footer>

<a class="wa" href="{WHATSAPP}" target="_blank" rel="noopener" aria-label="Fale no WhatsApp">✆ <span>Fale no WhatsApp</span></a>

<script>
  var t = document.getElementById('navToggle'), n = document.getElementById('navLinks');
  t.addEventListener('click', function () {{
    var open = n.classList.toggle('is-open');
    t.setAttribute('aria-expanded', open);
  }});
</script>"""


def page(*, title: str, description: str, path: str, body: str, og_type: str = "website",
         extra_head: str = "") -> str:
    url = SITE_URL + path
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(description)}">
<meta name="theme-color" content="#1D5C3A">
<link rel="canonical" href="{url}">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(description)}">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="{SITE_NAME}">
{HEAD_EXTRA}
<link rel="alternate" type="application/rss+xml" title="Blog TM Controladoria" href="/feed.xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,700;1,9..40,400&family=Playfair+Display:ital,wght@0,600;0,700;1,600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/styles.css">
<link rel="stylesheet" href="/blog.css">
{extra_head}
</head>
<body>

{header()}

{body}

{footer()}
</body>
</html>
"""


def post_card(p: Post) -> str:
    return f"""<article class="post-card">
  <a href="{p.url}">
    <span class="post-cat">{e(p.categoria)}</span>
    <h3>{e(p.titulo)}</h3>
    <p>{e(p.resumo)}</p>
    <span class="post-meta">{data_curta(p.data)} · {p.leitura} min de leitura</span>
  </a>
</article>"""


def chips(ativa: str | None, contagem: dict[str, int]) -> str:
    items = [f'<a class="chip{" is-active" if ativa is None else ""}" href="/blog/">Todos</a>']
    for c, s in CATEGORIES.items():
        if contagem.get(c):
            cls = " is-active" if ativa == c else ""
            items.append(f'<a class="chip{cls}" href="/blog/categoria/{s}/">{e(c)} <small>{contagem[c]}</small></a>')
    return '<nav class="chips" aria-label="Categorias">' + "".join(items) + "</nav>"


def pagination(base: str, atual: int, total: int) -> str:
    if total <= 1:
        return ""
    def href(n: int) -> str:
        return base if n == 1 else f"{base}pagina/{n}/"
    partes = []
    if atual > 1:
        partes.append(f'<a href="{href(atual - 1)}">← Anteriores</a>')
    partes.append(f"<span>Página {atual} de {total}</span>")
    if atual < total:
        partes.append(f'<a href="{href(atual + 1)}">Mais antigos →</a>')
    return '<nav class="pagination">' + "".join(partes) + "</nav>"


def listing_pages(posts: list[Post], base: str, titulo: str, subtitulo: str,
                  ativa: str | None, contagem: dict[str, int]) -> dict[str, str]:
    pages = {}
    total = max(1, -(-len(posts) // POSTS_PER_PAGE))
    for n in range(1, total + 1):
        lote = posts[(n - 1) * POSTS_PER_PAGE: n * POSTS_PER_PAGE]
        destaque = ""
        if n == 1 and lote and ativa is None:
            d, lote = lote[0], lote[1:]
            destaque = f"""<a class="post-featured" href="{d.url}">
      <span class="post-cat">{e(d.categoria)} · mais recente</span>
      <h2>{e(d.titulo)}</h2>
      <p>{e(d.resumo)}</p>
      <span class="post-meta">{data_curta(d.data)} · {d.leitura} min de leitura</span>
    </a>"""
        cards = "\n".join(post_card(p) for p in lote)
        vazio = '<p class="lead">Nenhum artigo publicado ainda.</p>' if not posts else ""
        path = base if n == 1 else f"{base}pagina/{n}/"
        sufixo = "" if n == 1 else f" (página {n})"
        body = f"""<section class="hero hero--blog">
  <div class="wrap">
    <span class="eyebrow">Blog TM Controladoria</span>
    <h1>{titulo}</h1>
    <p class="lead lead--light">{subtitulo}</p>
  </div>
</section>

<section class="section section--blog">
  <div class="wrap">
    {chips(ativa, contagem)}
    {destaque}
    <div class="post-grid">
{cards}
    </div>
    {vazio}
    {pagination(base, n, total)}
  </div>
</section>"""
        titulo_txt = re.sub(r"<[^>]+>", "", titulo)
        pages[path] = page(title=f"{titulo_txt}{sufixo} | Blog {SITE_NAME}", description=re.sub(r"<[^>]+>", "", subtitulo),
                           path=path, body=body)
    return pages


def post_page(p: Post, relacionados: list[Post]) -> str:
    fontes = "\n".join(f"<li>{fonte_html(f)}</li>" for f in p.fontes)
    rel = ""
    if relacionados:
        rel = f"""<section class="section section--tight soft">
  <div class="wrap">
    <h2 class="related-title">Leia também</h2>
    <div class="post-grid">
{chr(10).join(post_card(r) for r in relacionados)}
    </div>
  </div>
</section>"""
    atualizado = (f' · atualizado em <time datetime="{p.atualizado.isoformat()}">{data_br(p.atualizado)}</time>'
                  if p.atualizado else "")
    tags = ""
    if p.tags:
        tags = '<ul class="post-tags">' + "".join(f"<li>{e(t)}</li>" for t in p.tags) + "</ul>"
    ld = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": p.titulo,
        "description": p.resumo,
        "datePublished": p.data.isoformat(),
        "dateModified": (p.atualizado or p.data).isoformat(),
        "inLanguage": "pt-BR",
        "mainEntityOfPage": SITE_URL + p.url,
        "articleSection": p.categoria,
        "keywords": ", ".join(p.tags),
        "author": {"@type": "Organization", "name": SITE_NAME, "url": SITE_URL},
        "publisher": {"@type": "Organization", "name": SITE_NAME, "url": SITE_URL,
                      "logo": {"@type": "ImageObject", "url": SITE_URL + "/assets/icon-512.png"}},
        "image": OG_IMAGE,
    }
    extra = (f'<meta property="article:published_time" content="{p.data.isoformat()}">\n'
             f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>')
    body = f"""<section class="hero hero--post">
  <div class="wrap wrap--post">
    <nav class="breadcrumb" aria-label="Você está em"><a href="/">Início</a> / <a href="/blog/">Blog</a> / <a href="/blog/categoria/{p.cat_slug}/">{e(p.categoria)}</a></nav>
    <h1>{e(p.titulo)}</h1>
    <p class="lead lead--light">{e(p.resumo)}</p>
    <p class="post-byline">{e(p.autor)} · <time datetime="{p.data.isoformat()}">{data_br(p.data)}</time>{atualizado} · {p.leitura} min de leitura</p>
  </div>
</section>

<article class="section section--post">
  <div class="wrap wrap--post">
    <div class="prose">
{p.html}
    </div>
    {tags}

    <aside class="post-sources">
      <h2>Fontes e legislação</h2>
      <ul>
{fontes}
      </ul>
      <p class="post-disclaimer">Conteúdo informativo, atualizado na data de publicação. Regras tributárias mudam com frequência e cada caso tem particularidades. Antes de decidir, fale com um contador.</p>
    </aside>

    <div class="post-cta">
      <h2>Quer saber como isso afeta a sua empresa?</h2>
      <p>Conte a sua situação. A gente analisa e diz o que faria, sem proposta genérica.</p>
      <a class="btn btn--gold" href="{WHATSAPP}?text={e(quote_wa('Olá! Li o artigo “' + p.titulo + '” no blog e gostaria de conversar.'))}" target="_blank" rel="noopener">Falar no WhatsApp</a>
    </div>
  </div>
</article>

{rel}"""
    return page(title=f"{p.titulo} | {SITE_NAME}", description=p.resumo, path=p.url,
                body=body, og_type="article", extra_head=extra)


def quote_wa(text: str) -> str:
    from urllib.parse import quote
    return quote(text)


def fonte_html(f: str) -> str:
    """'Descrição | https://url' vira link; sem URL vira texto."""
    if "|" in f:
        desc, url = (x.strip() for x in f.rsplit("|", 1))
        if url.startswith("http"):
            return f'<a href="{e(url)}" target="_blank" rel="noopener">{e(desc)}</a>'
    return e(f)


def home_section(posts: list[Post]) -> str:
    if not posts:
        return ""
    cards = "\n".join(post_card(p) for p in posts[:3])
    return f"""<section class="section soft" id="blog">
  <div class="wrap">
    <div class="center">
      <span class="eyebrow eyebrow--dark">Blog</span>
      <h2>Contabilidade explicada para quem decide</h2>
      <p class="lead">Reforma Tributária, Simples Nacional, prazos e Imposto de Renda: o que mudou e o que fazer, em linguagem de dono de empresa.</p>
    </div>
    <div class="post-grid" style="margin-top:44px">
{cards}
    </div>
    <div class="cta-actions" style="margin-top:34px;justify-content:center">
      <a class="btn btn--outline" href="/blog/">Ver todos os artigos</a>
    </div>
  </div>
</section>"""


# --------------------------------------------------------------------------- #
# Arquivos auxiliares
# --------------------------------------------------------------------------- #
def feed(posts: list[Post]) -> str:
    def rfc822(d: date) -> str:
        return datetime(d.year, d.month, d.day, 6, 0, tzinfo=BRT).strftime("%a, %d %b %Y %H:%M:%S -0300")
    items = "\n".join(f"""  <item>
    <title>{e(p.titulo)}</title>
    <link>{SITE_URL}{p.url}</link>
    <guid>{SITE_URL}{p.url}</guid>
    <pubDate>{rfc822(p.data)}</pubDate>
    <category>{e(p.categoria)}</category>
    <description>{e(p.resumo)}</description>
  </item>""" for p in posts[:30])
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
  <title>Blog {SITE_NAME}</title>
  <link>{SITE_URL}/blog/</link>
  <description>Reforma Tributária, Simples Nacional, prazos e Imposto de Renda.</description>
  <language>pt-BR</language>
{items}
</channel>
</rss>
"""


def sitemap(posts: list[Post], paths: list[str]) -> str:
    urls = [f"  <url><loc>{SITE_URL}{p}</loc></url>" for p in paths]
    urls += [f"  <url><loc>{SITE_URL}{p.url}</loc><lastmod>{(p.atualizado or p.data).isoformat()}</lastmod></url>"
             for p in posts]
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n")


# Subpasta de publicação (ex.: "/tmcontroladoria-site" no endereço provisório do GitHub Pages).
# Vazio quando o site está na raiz do domínio próprio.
BASE_PATH = os.environ.get("BASE_PATH", "").rstrip("/")


def with_base(content: str) -> str:
    if not BASE_PATH:
        return content
    return re.sub(r'(href|src)="/(?!/)', rf'\1="{BASE_PATH}/', content)


def write(path: str, content: str) -> None:
    target = OUT / path.lstrip("/")
    if path.endswith("/"):
        target = target / "index.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.suffix == ".html":
        content = with_base(content)
    target.write_text(content, encoding="utf-8")


# --------------------------------------------------------------------------- #
def build(incluir_rascunhos: bool = False) -> list[Post]:
    posts = load_posts(incluir_rascunhos)
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()

    for name in STATIC_FILES:
        src = ROOT / name
        if name == "index.html":
            conteudo = src.read_text(encoding="utf-8").replace("<!-- BLOG:ULTIMOS -->", home_section(posts))
            (OUT / name).write_text(with_base(conteudo), encoding="utf-8")
        else:
            shutil.copy2(src, OUT / name)
    shutil.copytree(ROOT / "assets", OUT / "assets")
    shutil.copy2(ROOT / "assets" / "favicon.ico", OUT / "favicon.ico")
    # Arquivos de verificação (Google Search Console, Bing etc.) copiados sem alteração
    for src in list(ROOT.glob("google*.html")) + list(ROOT.glob("BingSiteAuth.xml")):
        shutil.copy2(src, OUT / src.name)

    contagem = {c: sum(1 for p in posts if p.categoria == c) for c in CATEGORIES}
    listados = ["/", "/parceiros.html", "/blog/"]

    for path, content in listing_pages(
            posts, "/blog/", "Contabilidade <em>sem complicação</em>",
            "Reforma Tributária, Simples Nacional, prazos e Imposto de Renda: o que mudou e o que fazer.",
            None, contagem).items():
        write(path, content)

    for cat, s in CATEGORIES.items():
        doc = [p for p in posts if p.categoria == cat]
        if not doc:
            continue
        base = f"/blog/categoria/{s}/"
        listados.append(base)
        for path, content in listing_pages(doc, base, e(cat), f"Todos os artigos sobre {cat.lower()}.",
                                           cat, contagem).items():
            write(path, content)

    for p in posts:
        mesma = [r for r in posts if r is not p and r.categoria == p.categoria]
        outras = [r for r in posts if r is not p and r.categoria != p.categoria]
        write(p.url, post_page(p, (mesma + outras)[:3]))

    write("/feed.xml", feed(posts))
    write("/sitemap.xml", sitemap(posts, listados))
    write("/robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n")
    (OUT / ".nojekyll").write_text("", encoding="utf-8")

    print(f"OK: {len(posts)} posts publicados em {OUT.relative_to(ROOT)}/")
    return posts


if __name__ == "__main__":
    build(incluir_rascunhos="--rascunhos" in sys.argv)
    if "--serve" in sys.argv:
        import functools
        import http.server
        handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(OUT))
        print("Servindo em http://localhost:8000 (Ctrl+C para parar)")
        http.server.ThreadingHTTPServer(("127.0.0.1", 8000), handler).serve_forever()
