---
titulo: "Como calcular o DAS do Simples Nacional: a alíquota efetiva explicada com números"
resumo: A alíquota da tabela não é a que você paga. Veja a fórmula da alíquota efetiva, um cálculo completo de DAS mês a mês e a regra especial para empresas abertas há menos de 12 meses.
data: 2026-11-15
categoria: Simples Nacional
tags: [Simples Nacional, DAS, alíquota efetiva, RBT12, PGDAS-D]
fontes:
  - Lei Complementar nº 123/2006, art. 18 e Anexos | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp123.htm
  - Resolução CGSN nº 140/2018 (arts. 21 a 25) | http://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=92278
  - Portal do Simples Nacional: PGDAS-D | https://www8.receita.fazenda.gov.br/SimplesNacional/
checagem:
  - Conferir a regra de RBT12 para empresas em início de atividade (1º mês: receita do mês × 12; meses seguintes: média dos meses anteriores × 12) no art. 22 da Resolução CGSN nº 140/2018
  - Conferir as alíquotas e parcelas a deduzir da 2ª, 3ª e 4ª faixas do Anexo I
---

Você abre a tabela do Simples Nacional, vê "alíquota de 9,5%" na sua faixa, multiplica pelo faturamento do mês e o número não bate com o DAS. Não é erro do sistema. A alíquota da tabela é a **nominal**. O que você paga é a **alíquota efetiva**, que sai de uma fórmula com dois ingredientes: o faturamento dos últimos 12 meses e a parcela a deduzir.

Entender essa conta ajuda a prever o imposto, a conferir o trabalho do contador e a não levar susto quando a empresa cresce.

## Os três números de que você precisa

1. **RBT12:** a receita bruta total dos 12 meses anteriores ao mês que está sendo apurado. Para o DAS de novembro, contam as receitas de novembro do ano passado até outubro deste ano.
2. **Alíquota nominal e parcela a deduzir:** estão na tabela do anexo da sua atividade, na faixa em que o RBT12 se encaixa.
3. **Receita do mês:** o que a empresa faturou no mês que está sendo apurado.

A fórmula é esta:

> **Alíquota efetiva = (RBT12 × alíquota nominal - parcela a deduzir) ÷ RBT12**
>
> **DAS do mês = receita do mês × alíquota efetiva**

## Exemplo completo: uma loja em Uberaba

Uma loja de roupas (comércio, Anexo I) faturou **R$ 540 mil nos últimos 12 meses** e **R$ 50 mil neste mês**.

O RBT12 de R$ 540 mil cai na 3ª faixa do Anexo I (de R$ 360 mil a R$ 720 mil), com alíquota nominal de 9,5% e parcela a deduzir de R$ 13.860.

- 540.000 × 9,5% = 51.300
- 51.300 - 13.860 = 37.440
- 37.440 ÷ 540.000 = **6,93%** (alíquota efetiva)
- DAS do mês: 50.000 × 6,93% = **R$ 3.466,67**

Repare que a loja paga 6,93%, e não 9,5%. A parcela a deduzir existe justamente para que a mudança de faixa não provoque um salto brusco no imposto.

## O que acontece quando a empresa cresce

Suponha que, um ano depois, o RBT12 da mesma loja tenha chegado a **R$ 760 mil**. Agora ela está na 4ª faixa (alíquota nominal de 10,7%, parcela a deduzir de R$ 22.500):

- 760.000 × 10,7% = 81.320
- 81.320 - 22.500 = 58.820
- 58.820 ÷ 760.000 = **7,74%**

Os mesmos R$ 50 mil de venda no mês geram DAS de **R$ 3.869,74**, cerca de R$ 403 a mais. A alíquota efetiva sobe aos poucos, conforme o faturamento acumulado. Por isso, quem projeta o caixa do ano que vem precisa projetar também a alíquota.

| | RBT12 de R$ 540 mil | RBT12 de R$ 760 mil |
|---|---|---|
| Faixa do Anexo I | 3ª | 4ª |
| Alíquota efetiva | 6,93% | 7,74% |
| DAS sobre R$ 50 mil | R$ 3.466,67 | R$ 3.869,74 |

## Empresa nova: como fica o RBT12

Quem abriu a empresa há menos de 12 meses não tem um ano inteiro de histórico. A Resolução CGSN nº 140/2018 resolve assim:

- **No primeiro mês de atividade**, o RBT12 é a própria receita do mês multiplicada por 12.
- **Nos meses seguintes, até completar 12**, usa-se a média das receitas dos meses anteriores multiplicada por 12.

Exemplo: uma loja abriu em setembro e faturou R$ 20 mil. Em outubro, faturou R$ 30 mil. Para o DAS de outubro, a média dos meses anteriores é R$ 20 mil, e o RBT12 fica em R$ 240 mil (2ª faixa: 7,3% e R$ 5.940).

- 240.000 × 7,3% = 17.520
- 17.520 - 5.940 = 11.580
- 11.580 ÷ 240.000 = **4,825%**
- DAS de outubro: 30.000 × 4,825% = **R$ 1.447,50**

Um primeiro mês muito forte "infla" o RBT12 dos meses seguintes. Vale ter isso em mente ao planejar a abertura e as primeiras vendas. Se você está nessa fase, veja também o [passo a passo para abrir empresa em Uberaba](/blog/abrir-empresa-passo-a-passo-uberaba/).

## Cuidados que mudam o resultado

- **Cada atividade tem seu anexo.** Se a empresa vende produtos e presta serviços, cada receita é calculada na sua tabela, sempre usando o RBT12 total da empresa. Veja [como saber o seu anexo](/blog/anexos-simples-nacional-como-saber-o-seu/).
- **Receitas monofásicas, com substituição tributária ou com ISS retido** têm parte dos tributos excluída do cálculo. Informar tudo como receita comum faz pagar a mais.
- **Regime de caixa ou de competência.** A empresa pode optar por apurar pela data do recebimento ou pela data da venda. A opção vale para o ano inteiro.
- **Faturamento perto de R$ 3,6 milhões** exige atenção ao sublimite de ICMS e ISS.

## O que fazer agora

1. Some o faturamento dos últimos 12 meses e encontre a sua faixa.
2. Aplique a fórmula e compare com o último DAS. Se a diferença for grande, pergunte ao contador como cada receita foi classificada.
3. Use a mesma conta para projetar 2027 com o crescimento esperado. É uma planilha simples que evita surpresa no caixa.
