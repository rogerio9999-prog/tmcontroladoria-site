# TM Controladoria — site e blog

Site institucional + blog da TM Controladoria e Soluções Contábeis (Uberaba/MG).
Público: donos de pequenas e médias empresas (Simples Nacional, Presumido), MEIs e pessoas físicas com renda além do salário.

## Estrutura

- `index.html`, `parceiros.html`, `styles.css` — páginas institucionais (HTML estático, editadas à mão).
- `blog.css` — estilos do blog.
- `posts/*.md` — um arquivo por artigo. **É aqui que o conteúdo diário entra.**
- `build.py` — gera o site completo em `_site/` (listagem, categorias, artigos, RSS, sitemap e os 3 últimos posts na home, no marcador `<!-- BLOG:ULTIMOS -->` do index.html).
- `.github/workflows/deploy.yml` — publica no GitHub Pages a cada push na `main` e todo dia às 06:00.

Comandos: `python build.py` (gera), `python build.py --serve` (gera e serve em localhost:8000), `python build.py --rascunhos` (inclui rascunhos e datas futuras).
O build **falha** se um post tiver campo obrigatório faltando, categoria inválida ou slug repetido. Rode-o sempre antes de abrir o PR.

## Formato de um post

Nome do arquivo: `posts/AAAA-MM-DD-slug-curto.md` (o slug vira a URL `/blog/slug-curto/`).

```markdown
---
titulo: "Título claro, com o benefício ou a dúvida do leitor"
resumo: Uma ou duas frases (até ~200 caracteres). Vira a meta description e o texto do card.
data: 2026-11-15
categoria: Simples Nacional
tags: [tag 1, tag 2, tag 3]
fontes:
  - Nome da norma ou página oficial | https://url-oficial
checagem:
  - Ponto que o revisor humano precisa conferir antes de aprovar
---

Texto em Markdown, começando direto pelo gancho (sem repetir o título).
```

- Use aspas no título quando ele tiver dois-pontos no início ou caracteres especiais.
- Categorias válidas (exatamente assim): `Reforma Tributária`, `Simples Nacional`, `MEI`, `Prazos e Agenda`, `Pessoa Física`, `Trabalhista e Folha`, `Gestão e Controladoria`.
- Campos opcionais: `atualizado: AAAA-MM-DD`, `rascunho: true`, `autor`, `slug`.
- `checagem` **não aparece no site**: serve só para a revisão. Liste nele toda afirmação de que você não tem certeza absoluta (alíquotas, prazos, números de normas, links).
- Post com `data` futura só aparece no site a partir daquele dia (o deploy roda diariamente às 06:00).

## Rotina diária: 5 posts

Todo dia, produzir **5 posts**, um de cada linha editorial abaixo, em **um único Pull Request** (`posts/AAAA-MM-DD`) para revisão. **Nunca fazer push direto na `main`.**

1. **Notícia do dia.** Uma norma, decisão ou mudança publicada recentemente (DOU, Receita Federal, CGSN, Comitê Gestor do IBS, SEF-MG, Prefeitura de Uberaba, eSocial). Explicar o que muda e para quem. Se não houver novidade relevante, trocar por mais um guia prático.
2. **Reforma Tributária na prática.** Série contínua sobre CBS/IBS: cronograma, NF-e, cClassTrib, créditos, Simples × regime regular, split payment, precificação, contratos. Sempre com exemplo concreto.
3. **Prazos e agenda.** O que vence nos próximos 7 a 15 dias (DAS, DCTFWeb, FGTS, EFD-Reinf, DEFIS, DASN-SIMEI, IRPF, 13º etc.), com as datas já ajustadas para fins de semana e feriados.
4. **Pergunta de cliente.** Uma dúvida real e específica respondida de forma direta ("Sou MEI e contratei um funcionário, e agora?").
5. **Guia definitivo.** Conteúdo atemporal e mais longo sobre um tema muito buscado (Fator R, pró-labore, abertura de empresa, carnê-leão, ganho de capital).

Antes de escrever, **liste os arquivos em `posts/`** e não repita temas já cobertos nos últimos 60 dias. Se um tema antigo mudou, prefira atualizar o post existente (campo `atualizado`) a criar um novo.

### Regras de conteúdo (obrigatórias)

- **Precisão acima de tudo.** Não inventar números, alíquotas, prazos, números de lei ou de instrução normativa. Se não tiver certeza, pesquise na fonte oficial; se ainda assim não tiver, escreva de forma que não dependa do número e registre o ponto em `checagem`.
- **Fontes oficiais** em `fontes`, com link: Planalto, Receita Federal, Portal do Simples Nacional, gov.br, DOU, CFC, SEF-MG. Nada de blogs de terceiros como fonte.
- **Datas:** confira o dia da semana de qualquer prazo citado e ajuste para o dia útil correto.
- **Sem promessas** ("pague menos imposto garantido", "zere seus tributos"). Nada de sensacionalismo. A publicidade contábil deve ser sóbria.
- **Sem conselho individual definitivo**: o texto explica a regra e mostra o raciocínio; a decisão do caso concreto é "fale com um contador".
- Não citar clientes, nem valores ou situações reais de clientes.

### Estilo

- Português do Brasil, tom de contador experiente conversando com um dono de empresa: claro, direto, sem juridiquês. Explicar siglas na primeira vez.
- **Nunca use travessão (— ou –)**, em nenhuma parte do post (título, resumo, texto, fontes). Use vírgula, dois-pontos, parênteses ou ponto final. O texto deve soar escrito por uma pessoa. O `build.py` recusa posts com travessão. O hífen comum (-) em palavras compostas continua permitido.
- Evite também outros vícios de texto gerado por IA: frases de efeito vazias ("Não é só X, é Y"), listas de três adjetivos, "Em resumo", "Vale ressaltar", "É importante destacar". Prefira frases curtas e concretas.
- 700 a 1.300 palavras (guia definitivo: até 2.000).
- Abrir com o problema do leitor, não com definição de dicionário.
- Use subtítulos `##`, listas curtas, **um exemplo numérico** sempre que houver cálculo e tabelas quando houver comparação.
- Linkar 1 ou 2 posts relacionados do próprio blog (`/blog/slug/`).
- Quando fizer sentido, mencionar Uberaba ou o Triângulo Mineiro (SEO local), sem forçar.
- Terminar com um "o que fazer agora" prático. O CTA de WhatsApp já é inserido automaticamente: não repita.

### Revisão final (obrigatória, antes de abrir o PR)

Os posts são **publicados automaticamente ao meio-dia** se ninguém intervier. Por isso, depois de escrever os 5 posts, releia cada um como revisor:

1. Para **cada** número, alíquota, valor, prazo e número de norma citado, confirme na fonte oficial (WebFetch). Se não confirmar, corrija ou reescreva o trecho sem depender do número.
2. Refaça as contas dos exemplos numéricos com Python.
3. Confira que cada link em `fontes` abre (WebFetch) e trata do assunto citado.
4. Classifique o que sobrou em `checagem`:
   - **Detalhe menor** (ex.: confirmar link alternativo, redação): o post segue normalmente.
   - **Dúvida relevante** (um número, prazo, regra ou alcance da norma que você não conseguiu confirmar e que pode levar o leitor a erro): **não use `rascunho: true`**. Todos os 5 posts devem ir ao ar no horário. Reescreva o trecho para que ele não dependa da informação não confirmada (explique a regra de forma geral, sem o número, e oriente o leitor a confirmar com o contador) ou retire o trecho. Se o post inteiro depender dela, troque o tema por outro da mesma linha editorial que você consiga confirmar. Registre o ponto em `checagem`.

Os posts da rotina diária nunca são marcados como rascunho: prefira um texto mais geral e correto a um texto específico e duvidoso.

### Pull Request

Título: `Posts de DD/MM/AAAA`. No corpo, para cada post: título, linha editorial, resumo em uma frase, os pontos que foram reescritos de forma geral por falta de confirmação, se houver, e a lista `checagem` copiada do arquivo, para o revisor ir direto aos pontos de risco.

### Publicação automática

`.github/workflows/auto-publicar.yml` faz o merge dos PRs `posts/...` todo dia por volta do meio-dia (11:47 de Brasília, com segunda tentativa às 12:53), exceto os marcados com a etiqueta `segurar`, os fechados e os que falharam na validação. Posts com `rascunho: true` não aparecem no site; para liberar um, edite o arquivo e mude para `rascunho: false`.
