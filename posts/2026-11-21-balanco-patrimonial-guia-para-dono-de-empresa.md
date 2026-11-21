---
titulo: "Balanço patrimonial: guia para o dono de empresa entender o que está lendo"
resumo: O balanço mostra o que a empresa tem, o que deve e o que sobra para os sócios. Veja cada grupo de contas, como ler os indicadores principais, um exemplo com números e os erros mais comuns de leitura.
data: 2026-11-21
categoria: Gestão e Controladoria
tags: [balanço patrimonial, contabilidade, ativo, passivo, patrimônio líquido, indicadores, liquidez]
fontes:
  - Lei nº 6.404/1976 (Lei das Sociedades por Ações), art. 178 (grupos do balanço), Planalto | https://www.planalto.gov.br/ccivil_03/leis/l6404compilada.htm
  - Conselho Federal de Contabilidade, Normas Brasileiras de Contabilidade | https://cfc.org.br/
  - Código Civil, arts. 1.179 a 1.195 (escrituração e balanço), Planalto | https://www.planalto.gov.br/ccivil_03/leis/2002/l10406compilada.htm
checagem:
  - Confirmar a numeração do art. 178 da Lei 6.404/1976 (classificação das contas do ativo e do passivo) e dos artigos do Código Civil sobre balanço
  - O texto usa uma classificação simplificada; confirmar com o contador a classificação adotada pela empresa (NBC TG 1000 para pequenas e médias empresas, quando aplicável)
  - Os valores do exemplo são ilustrativos; os índices foram recalculados em Python
  - Confirmar os links de fontes
  - Os links de fontes oficiais não puderam ser abertos durante a redação (rede do ambiente restrita); regras escritas de forma geral, conferir antes de aprovar
---

O contador entrega o balanço no fim do ano, o dono dá uma olhada no lucro lá embaixo e guarda o PDF. Um erro comum, e caro: o balanço tem muito mais informação do que o lucro. Ele mostra se a empresa consegue pagar as contas dos próximos meses, quanto depende de dívida e quanto realmente pertence aos sócios.

## A ideia por trás do balanço

O balanço patrimonial é uma **fotografia** da empresa em uma data, geralmente 31 de dezembro. Ele tem dois lados que sempre fecham:

**Ativo = Passivo + Patrimônio Líquido**

- **Ativo:** o que a empresa tem e controla (dinheiro, valores a receber, estoque, máquinas, imóveis).
- **Passivo:** o que a empresa deve (fornecedores, impostos, salários, empréstimos).
- **Patrimônio líquido:** o que sobra para os sócios depois de pagar tudo (capital investido mais os lucros retidos).

A DRE (Demonstração do Resultado) é diferente: é um **filme** de um período, que mostra receitas e despesas. Para ler a DRE, veja [DRE da pequena empresa](/blog/dre-pequena-empresa-como-ler/).

## Os grupos de contas

**Ativo circulante:** o que vira dinheiro em até 12 meses. Caixa e bancos, clientes a receber, estoques.

**Ativo não circulante:** o que fica por mais tempo. Imóveis, veículos, máquinas, investimentos de longo prazo.

**Passivo circulante:** o que vence em até 12 meses. Fornecedores, folha e encargos a pagar, impostos a recolher, parcelas de empréstimo do próximo ano.

**Passivo não circulante:** dívidas com vencimento além de 12 meses.

**Patrimônio líquido:** capital social, reservas e lucros acumulados (ou prejuízos).

## Exemplo com números

Uma loja em Uberaba, em 31/12 (valores ilustrativos):

| Ativo | R$ | Passivo e patrimônio líquido | R$ |
|---|---|---|---|
| Caixa e bancos | 18.000 | Fornecedores | 25.000 |
| Clientes a receber | 42.000 | Impostos a pagar | 9.000 |
| Estoque | 30.000 | Folha e encargos a pagar | 14.000 |
| **Ativo circulante** | **90.000** | Empréstimo (curto prazo) | 12.000 |
| Imobilizado (móveis, equipamentos) | 60.000 | **Passivo circulante** | **60.000** |
| **Ativo não circulante** | **60.000** | Empréstimo (longo prazo) | 20.000 |
| | | **Patrimônio líquido** | **70.000** |
| **Total do ativo** | **150.000** | **Total passivo + PL** | **150.000** |

Conferindo: 60.000 + 20.000 + 70.000 = 150.000, igual ao ativo. O balanço fecha.

## Três leituras que mudam decisões

**1. Liquidez corrente = ativo circulante ÷ passivo circulante**
90.000 ÷ 60.000 = **1,5**. Para cada R$ 1 que vence em até 12 meses, a empresa tem R$ 1,50 que vira dinheiro no mesmo período. Acima de 1 é, em geral, confortável, mas depende da qualidade do ativo: estoque parado e cliente que não paga não são dinheiro de verdade.

**2. Endividamento = (passivo circulante + não circulante) ÷ ativo total**
(60.000 + 20.000) ÷ 150.000 = **53%**. Pouco mais da metade do que a empresa tem foi financiada por terceiros. O que é aceitável varia por setor; o importante é acompanhar a evolução de um ano para o outro.

**3. Patrimônio líquido ao longo do tempo**
Se o patrimônio líquido cresce ano a ano, a empresa está retendo lucro. Se encolhe, ou o resultado é negativo, ou os sócios estão retirando mais do que a empresa ganha. Veja a relação com [distribuição de lucros](/blog/distribuicao-lucros-sem-contabilidade-risco/).

Para outros números úteis, veja [indicadores financeiros da pequena empresa](/blog/indicadores-financeiros-pequena-empresa/).

## Erros comuns de leitura

- **Olhar só o caixa.** A empresa pode ter R$ 18.000 em caixa e R$ 60.000 para pagar no ano.
- **Ignorar o estoque.** Estoque antigo, sem giro, está no ativo pelo custo, mas pode valer menos. Veja [estoque parado](/blog/estoque-parado-quanto-custa/).
- **Confundir lucro com caixa.** Lucro contábil não é dinheiro disponível; parte está em clientes e estoque.
- **Contas de sócio misturadas.** Quando o dono paga conta pessoal com dinheiro da empresa, o balanço fica distorcido. Veja [separar finanças pessoais e da empresa](/blog/separar-financas-pessoa-fisica-empresa/).
- **Balanço sem conciliação.** Se o banco, os clientes e os fornecedores não foram conferidos, o balanço pode estar bonito e errado.

## Quem precisa fazer balanço

A obrigação depende do porte e do regime. Empresas do Simples Nacional têm regras próprias de escrituração, e muitas fazem balanço mesmo quando a lei permite algo mais simples, porque banco, investidor ou sócio pedem. Veja [escrituração contábil no Simples](/blog/escrituracao-contabil-empresa-simples-obrigatoria/). Para o seu caso, o contador confirma o que se aplica.

## Perguntas para fazer ao contador

1. O que o balanço mostra sobre a minha liquidez no próximo trimestre?
2. Quanto do meu ativo é estoque e cliente a receber, e qual a idade disso?
3. Meu patrimônio líquido cresceu ou caiu no ano? Por quê?
4. Há contas de sócios, empréstimos ou saldos antigos que precisam ser regularizados?
5. As contas do balanço batem com banco, folha e impostos?

## O que fazer agora

- Peça ao contador o balanço (ou o balancete mais recente) e calcule a liquidez e o endividamento com as fórmulas acima.
- Anote os números e compare com o fechamento do ano que vem.
- Reserve uma conversa de 30 minutos com o contador para tirar dúvidas, antes de decidir sobre retirada de lucros, investimento ou empréstimo.
- Para organizar o fechamento do ano, veja o [checklist de fechamento contábil](/blog/fechamento-contabil-fim-de-ano-checklist/).
