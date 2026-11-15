---
titulo: "cClassTrib e CST do IBS e da CBS: como revisar o cadastro de produtos para a NF-e"
resumo: A nota fiscal ganhou campos novos para CBS e IBS, e o sistema só calcula certo se cada produto estiver bem classificado. Veja o que é o cClassTrib, como ele se liga ao CST e como fazer a revisão do cadastro.
data: 2026-11-15
categoria: Reforma Tributária
tags: [cClassTrib, CST, NF-e, cadastro de produtos, IBS, CBS]
fontes:
  - Portal Nacional da NF-e (notas técnicas e tabelas de classificação do IBS e da CBS) | https://www.nfe.fazenda.gov.br/portal/principal.aspx
  - Lei Complementar nº 214/2025, texto compilado | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214compilado.htm
  - Ministério da Fazenda, regulamento da CBS e do IBS (obrigatoriedade a partir de agosto de 2026) | https://www.gov.br/fazenda/pt-br/assuntos/noticias/2026/abril/regulamento-detalha-as-regras-que-apresentam-sistema-mais-simples-transparente-e-previsivel-para-cidadaos-e-empresas
checagem:
  - Confirmar que o cClassTrib tem seis dígitos e que os três primeiros correspondem ao CST, conforme a tabela vigente do Informe Técnico 2025.002 no Portal da NF-e
  - Confirmar a data de exigência dos campos de IBS e CBS para optantes do Simples e MEI em produção (fontes de mercado citam 04/01/2027, com base na NT 2025.002; a NT 2026.005 de 30/10/2026 trata do Simples)
  - A alíquota cheia de 26% do exemplo é HIPOTÉTICA
  - O link do Portal Nacional da NF-e entrou em loop de redirecionamento na verificação automática; confirmar no navegador que abre (detalhe menor)
---

Desde agosto de 2026, empresas fora do Simples Nacional precisam preencher na nota fiscal as informações de CBS e IBS. Muita gente resolveu isso "no padrão" do sistema, marcando todos os produtos como tributação integral. Funciona para passar a nota, mas é um erro que vai custar caro a partir de 2027, quando os valores deixam de ser simbólicos.

O que define se o cálculo sai certo é a combinação de três informações no cadastro de cada produto: **NCM, CST e cClassTrib**.

## As três peças

**NCM** (Nomenclatura Comum do Mercosul) é o código que identifica o produto. Você já usa hoje. Na Reforma, ele continua sendo a porta de entrada: é pelo NCM que a lei define quem tem alíquota zero, redução de 60% e outros tratamentos.

**CST do IBS e da CBS** (Código de Situação Tributária) indica a situação da operação: tributação integral, alíquota reduzida, isenção, suspensão, diferimento e assim por diante.

**cClassTrib** (código de classificação tributária) detalha o CST. Ele aponta o fundamento legal exato do tratamento e diz ao sistema qual percentual de redução aplicar. As tabelas oficiais ficam no Portal Nacional da NF-e e são atualizadas com frequência.

## Como as peças se encaixam

| Produto | Tratamento na LC 214/2025 | O que o cadastro precisa indicar |
|---|---|---|
| Arroz | Cesta Básica Nacional, alíquota zero | CST e cClassTrib de alíquota zero, com o fundamento da cesta básica |
| Medicamento listado | Redução de 60% | CST de alíquota reduzida e cClassTrib do inciso correspondente |
| Ferramenta elétrica | Tributação integral | CST e cClassTrib de tributação integral |

Se o cClassTrib estiver errado, o sistema aplica a alíquota errada, e o erro passa para a nota, para a apuração e, no futuro, para a retenção no [split payment](/blog/split-payment-como-vai-funcionar/).

## Exemplo do custo de um erro

Um atacadista de Uberaba vende R$ 1.000 de um produto que tem direito à redução de 60%, mas está cadastrado como tributação integral. Com uma **alíquota cheia hipotética de 26%** (o número real ainda está sendo fixado):

| Cenário | Cálculo | Tributo destacado |
|---|---|---|
| Cadastro certo (redução de 60%) | R$ 1.000 × 26% × 40% | R$ 104 |
| Cadastro errado (integral) | R$ 1.000 × 26% | R$ 260 |
| **Diferença por venda** | | **R$ 156** |

Se o cliente é consumidor final, você cobrou R$ 156 a mais e ficou menos competitivo. Se o erro for o inverso (produto integral cadastrado com redução), você recolhe a menos e fica exposto a autuação. Multiplique pelo volume do ano e o problema aparece.

## Passo a passo da revisão

1. **Exporte o cadastro** do sistema com código interno, descrição, NCM, CST e cClassTrib atuais.
2. **Confira o NCM** de cada item. NCM errado contamina tudo o que vem depois.
3. **Separe os itens com tratamento diferenciado**: alimentos, medicamentos, produtos de higiene, insumos agropecuários, dispositivos médicos e outros que a LC 214/2025 lista nos anexos. Veja [Redução de 60% de IBS e CBS](/blog/reducao-60-por-cento-ibs-cbs-setores/) e [Cesta Básica Nacional](/blog/cesta-basica-nacional-aliquota-zero/).
4. **Atribua CST e cClassTrib** a partir da tabela oficial mais recente, item por item, e anote o fundamento legal em um campo de observação.
5. **Teste no ambiente de homologação** do emissor, com notas de cada tipo de operação (venda, devolução, bonificação, remessa).
6. **Defina um responsável** por acompanhar as atualizações da tabela no Portal da NF-e.

## E se a empresa é do Simples Nacional?

O Simples ficou dispensado desses campos em 2026. A exigência para optantes e MEI está prevista para o início de 2027, com regras próprias publicadas em nota técnica em outubro de 2026. Não deixe para a primeira semana de janeiro: a revisão do cadastro é a mesma, e o emissor precisa estar atualizado antes.

## Serviços também entram

Quem emite NFS-e (nota de serviço) também precisa informar a classificação do serviço para IBS e CBS. Para prestadores, o ponto de atenção é o código do serviço e o enquadramento em reduções, como a de 30% para algumas profissões regulamentadas. Veja [Redução de 30% para profissionais liberais](/blog/reducao-30-por-cento-profissionais-liberais/).

## O que fazer agora

1. **Peça ao seu fornecedor de sistema** a versão que já traz as tabelas de CST e cClassTrib atualizadas.
2. **Revise primeiro os 20% de itens que geram 80% do faturamento.**
3. **Documente a classificação** de cada produto com o fundamento legal.
4. **Revise junto com seu contador** os itens com redução ou alíquota zero, que são os de maior risco.
5. Leia também [Como preparar o sistema emissor de notas para 2027](/blog/preparar-sistema-emissor-nota-2027-reforma/).
