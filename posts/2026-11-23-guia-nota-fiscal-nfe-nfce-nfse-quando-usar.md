---
titulo: "Guia definitivo da nota fiscal: NF-e, NFC-e e NFS-e, quando usar cada uma e os erros mais comuns"
resumo: Vendeu produto, prestou serviço ou atendeu no balcão? Cada operação pede um tipo de nota. Veja a diferença entre NF-e, NFC-e e NFS-e, quem emite o quê, como o MEI se encaixa e como evitar erros.
data: 2026-11-23
categoria: Gestão e Controladoria
tags: [nota fiscal, NF-e, NFC-e, NFS-e, MEI, Simples Nacional, ICMS, ISS, Uberaba]
fontes:
  - Portal Nacional da NF-e | https://www.nfe.fazenda.gov.br/
  - Portal da NFS-e Nacional (gov.br) | https://www.gov.br/nfse/pt-br
  - Lei Complementar nº 116/2003 (ISS), Planalto | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp116.htm
  - Secretaria de Estado de Fazenda de Minas Gerais | https://www.fazenda.mg.gov.br/
checagem:
  - Confirmar na legislação estadual de MG quando a NFC-e é obrigatória no varejo e as regras de cancelamento (o texto não cita prazos nem valores)
  - Confirmar na legislação do MEI (resolução do CGSN) a regra de emitir nota para pessoa jurídica e de dispensa para pessoa física, quando o cliente não pede
  - Confirmar no portal da prefeitura de Uberaba o sistema de emissão de NFS-e adotado hoje (padrão nacional ou sistema municipal)
  - Os links de fontes não puderam ser abertos durante a redação (rede do ambiente restrita)
---

"Emito nota para tudo?" Quase todo dono de empresa já fez essa pergunta, e a resposta depende do que está sendo vendido, para quem e de onde. Este guia reúne o que você precisa para escolher a nota certa, sem entrar em detalhes que mudam de estado para estado.

## A regra de bolso

A nota fiscal registra uma operação para o Fisco. Há três famílias principais, cada uma ligada a um tributo:

| Nota | Para quê | Tributo principal | Quem autoriza |
|---|---|---|---|
| **NF-e** | Venda de mercadoria entre empresas ou para consumidor, e outras operações com produto | ICMS (e IPI, quando há indústria) | Secretaria da Fazenda do estado |
| **NFC-e** | Venda de mercadoria para consumidor final no balcão | ICMS | Secretaria da Fazenda do estado |
| **NFS-e** | Prestação de serviço | ISS | Prefeitura (ou o ambiente nacional) |

Quem vende **produto** pensa em NF-e ou NFC-e. Quem presta **serviço** pensa em NFS-e. Quem faz as duas coisas emite as duas. Um erro comum é emitir nota de serviço de algo que é venda de mercadoria, e vice-versa.

## NF-e: o que é e quando usar

É a nota eletrônica de mercadoria, usada principalmente em vendas para outras empresas, remessas, devoluções e transferências. Ela carrega os dados do destinatário, os produtos com seus códigos e os tributos.

Pontos de atenção:

- O **cadastro do produto** (NCM e demais códigos) define a tributação. Código errado vira erro de imposto. Veja [CSOSN na nota fiscal do Simples](/blog/csosn-nota-fiscal-simples/).
- Se o cliente devolve a mercadoria, a devolução também precisa ser documentada. Veja [cliente devolveu a mercadoria](/blog/cliente-devolveu-mercadoria-como-fica-o-das/).
- Com a Reforma Tributária, os campos da NF-e ganham novas informações. Veja [cClassTrib e cadastro de produtos](/blog/cclasstrib-cst-nfe-cadastro-produtos/).

## NFC-e: o balcão do varejo

A NFC-e é a nota do consumidor final, no lugar do antigo cupom fiscal. É emitida no caixa, com ou sem CPF do cliente. A obrigatoriedade para cada tipo de varejo é definida pelo estado, então confirme com o contador a regra de Minas Gerais para a sua atividade.

Pontos de atenção:

- O sistema de caixa precisa estar integrado ao emissor.
- Venda por aplicativo ou site costuma exigir emissão também. Veja [e-commerce no Simples](/blog/simples-nacional-ecommerce-marketplace/).

## NFS-e: serviço e prefeitura

A nota de serviço é emitida segundo as regras da prefeitura. Hoje existe o **padrão nacional**, que reúne o ambiente de emissão e padroniza os campos. Veja [NFS-e padrão nacional](/blog/nfs-e-padrao-nacional-empresas/). Para saber como funciona em Uberaba, consulte o site da prefeitura e peça confirmação ao contador.

Pontos de atenção:

- **Descrição e código do serviço** precisam combinar com a atividade registrada no CNPJ. Veja [alterar CNAE](/blog/alterar-cnae-simples-nacional-impactos/).
- A **retenção de ISS** muda o valor líquido recebido. Veja [retenção de ISS](/blog/retencao-iss-empresa-simples-nacional/).
- O valor da nota deve bater com o valor recebido, para que a receita não fique escondida.

## E o MEI?

O MEI também emite nota, mas com regras próprias. Em linhas gerais, o MEI **deve emitir nota quando vende ou presta serviço para pessoa jurídica**, e para pessoa física costuma emitir quando o cliente pede (confirme essa regra com o contador). Veja [nota de serviço do MEI](/blog/mei-nota-fiscal-servico-padrao-nacional/). Ao passar de MEI para microempresa, as obrigações crescem. Veja [de MEI para microempresa](/blog/de-mei-para-microempresa-o-que-muda/).

## Exemplo: três vendas no mesmo dia

Uma empresa de Uberaba que vende e instala ar-condicionado fez três operações em um dia:

1. **Venda de um aparelho de R$ 3.200 para um consumidor no balcão:** NFC-e.
2. **Venda de dois aparelhos de R$ 6.400 (total) para uma empresa:** NF-e.
3. **Serviço de instalação de R$ 450 na casa do cliente:** NFS-e.

Total faturado: 3.200 + 6.400 + 450 = R$ 10.050. Esse total alimenta a receita do mês no PGDAS-D, separada por atividade (comércio e serviço). Veja [várias atividades no Simples](/blog/varias-atividades-simples-segregar-anexos/).

Se o instalador emitisse uma única NF-e com tudo, misturaria produto e serviço e geraria erro de imposto.

## Erros mais comuns

- **Emitir nota com valor menor** do que o cobrado.
- **Não emitir nota** para cliente pessoa física porque "ele não pediu". Veja [nota fiscal emitida errada](/blog/nota-fiscal-emitida-errada-cancelar-corrigir/).
- **Usar o mesmo código** para todos os produtos ou serviços.
- **Digitar dados do cliente errados** (CNPJ, endereço, inscrição estadual).
- **Perder o prazo de correção.** Cada tipo de nota tem regras de cancelamento e de carta de correção que variam; consulte o contador logo após notar o erro.
- **Não guardar o arquivo XML.** Veja [quanto tempo guardar documentos](/blog/guia-quanto-tempo-guardar-documentos-empresa/).

## Certificado digital e sistema emissor

Para emitir NF-e e NFC-e, normalmente é preciso certificado digital e um sistema emissor. Veja [certificado A1 e A3](/blog/certificado-digital-a1-a3-empresa/). Em 2027, o sistema precisará suportar os campos novos. Veja [preparar o sistema emissor](/blog/preparar-sistema-emissor-nota-2027-reforma/).

## Checklist antes de emitir

1. É mercadoria, serviço ou os dois?
2. Quem é o cliente (consumidor final ou empresa)?
3. O produto ou serviço está cadastrado com o código certo?
4. O valor da nota é o mesmo que será recebido?
5. Existe retenção de imposto a destacar?
6. O XML vai ser guardado?

## Como a nota conversa com a contabilidade e o imposto

Cada nota emitida alimenta o DAS, a escrituração e as declarações. O contador usa as notas para apurar a receita do mês e conferir se o que entrou no banco bate com o que foi faturado. Quando a nota é emitida errada ou fica de fora, o desencontro aparece no fechamento, e corrigir meses depois é trabalhoso.

Por isso vale ter uma rotina simples: emitir a nota no mesmo dia da operação, enviar o arquivo ao contador toda semana ou todo mês, e conciliar os recebimentos com as notas. Veja [conciliação bancária passo a passo](/blog/conciliacao-bancaria-passo-a-passo/).

## O que fazer agora

- Liste as operações que a sua empresa faz e associe cada uma ao tipo de nota.
- Peça ao contador para revisar o cadastro de produtos e serviços.
- Se o sistema emite uma nota "genérica" para tudo, procure trocar.
- Em caso de dúvida em uma operação específica, pergunte antes de emitir. Corrigir depois custa mais.
