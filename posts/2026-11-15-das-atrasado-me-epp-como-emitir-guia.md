---
titulo: "DAS atrasado da ME ou EPP: como emitir a guia certa e quanto custa pagar depois do dia 20"
resumo: O caminho para gerar o DAS em atraso muda conforme a idade do débito. Veja quando usar Gerar DAS, quando usar o menu Débitos, como a multa e os juros são calculados e o que fazer se o débito já foi para a dívida ativa.
data: 2026-11-15
categoria: Simples Nacional
tags: [Simples Nacional, DAS atrasado, PGDAS-D, multa de mora, juros Selic]
fontes:
  - Lei Complementar nº 123/2006, art. 35 (juros e multa pelas regras do imposto de renda) | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp123.htm
  - Lei nº 9.430/1996, art. 5º, § 3º, e art. 61 (multa de 0,33% ao dia, limite de 20%, juros Selic) | https://www.planalto.gov.br/ccivil_03/leis/l9430.htm
  - Manual do PGDAS-D 2018 (itens 6.8 e 7, Gerar DAS e DAS de cobrança) | https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/MANUAL_PGDAS-D_2018_V4.pdf
  - Perguntas e Respostas do Simples Nacional (pergunta 6.8, prazo do DAS) | https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/PerguntaoSN.pdf
  - Lei nº 14.759/2023 (feriado nacional de 20 de novembro) | https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/L14759.htm
  - Portal Regularize da PGFN | https://www.regularize.pgfn.gov.br/
checagem:
  - Confirmar no PGDAS-D atual se a opção Consolidar para outra data continua limitada a dia útil do mês corrente, como descreve o manual
  - O exemplo numérico não depende da Selic porque o pagamento ocorre no mês seguinte ao vencimento; conferir que a explicação dos juros (Selic dos meses intermediários mais 1% no mês do pagamento) está alinhada ao art. 61, § 3º, da Lei nº 9.430/1996
  - Conferir se o nome do serviço da PGFN para emitir o DAS de dívida ativa no Regularize continua o mesmo
---

O DAS do mês passou do vencimento e você entrou no Portal do Simples para gerar uma guia nova. Só que a tela não mostra o valor que você esperava, ou o sistema simplesmente não deixa emitir. Isso acontece porque, no Simples Nacional, **o caminho para gerar o DAS atrasado depende da idade do débito e de onde ele está sendo cobrado**. Escolher o menu errado gera guia com valor errado ou guia que nem chega a existir.

Este texto vale para microempresa (ME) e empresa de pequeno porte (EPP). O MEI usa outro sistema, o PGMEI, e tem um texto próprio: [DAS do MEI atrasado](/blog/mei-das-atrasado-consequencias-parcelamento/).

## Primeiro, o vencimento correto

O DAS vence no **dia 20 do mês seguinte** ao da receita. Se não houver expediente bancário no dia 20, o prazo passa automaticamente para o primeiro dia útil seguinte.

Um caso prático deste mês: o DAS de outubro de 2026 venceria em 20/11/2026, uma sexta-feira. Como 20 de novembro é feriado nacional (Lei nº 14.759/2023), o vencimento passa para **segunda-feira, 23/11/2026**. Quem paga nessa segunda não está atrasado.

## Os três caminhos para emitir a guia

O PGDAS-D (o programa de cálculo e declaração do Simples) oferece rotas diferentes. Antes de qualquer coisa, a apuração do mês precisa ter sido transmitida: **não existe DAS sem declaração transmitida**.

| Situação do débito | Onde gerar a guia |
|---|---|
| Venceu há pouco, ainda no mês seguinte ao vencimento | Declaração Mensal > Gerar DAS > Consolidar para outra data |
| Venceu há mais tempo, já está no sistema de cobrança da Receita | Débitos > Consultar/Gerar DAS (o chamado DAS Cobrança) |
| Já foi enviado para dívida ativa da União | Portal Regularize, da Procuradoria-Geral da Fazenda Nacional (PGFN) |

### 1. Consolidar para outra data

Logo depois do vencimento, a função **Gerar DAS** do menu Declaração Mensal ainda funciona. O botão "Consolidar para outra data" recalcula multa e juros para o dia em que você vai pagar. Segundo o manual do PGDAS-D, a data escolhida precisa ser um dia útil do mês corrente. Não adianta gerar hoje com data de hoje e pagar daqui a uma semana: a guia perde a validade.

### 2. Menu Débitos

Quando o débito já está em cobrança na Receita Federal, o caminho é **Débitos > Consultar/Gerar DAS**. Essa tela mostra o saldo "líquido", já descontando pagamentos parciais, compensações e parcelamentos. É também a rota obrigatória se você compensou parte do débito vencido: o Gerar DAS comum ignora a compensação e emite a guia pelo valor cheio.

Para períodos a partir de 2018, dá para marcar vários meses e gerar **um único DAS** para todos eles.

### 3. Débito na dívida ativa

O PGDAS-D bloqueia a emissão de guia para período cujo débito já foi enviado à PGFN ou transferido a estado ou município conveniado. Nesse caso:

- a parte federal é paga com DAS emitido no **Regularize**, da PGFN, onde também se negocia parcelamento ou transação;
- ICMS e ISS transferidos ao ente conveniado são pagos em **guia própria** do estado ou do município. Em Uberaba, isso significa tratar o ISS com a Prefeitura e o ICMS com a Secretaria de Estado de Fazenda de Minas Gerais (SEF-MG).

## Quanto custa o atraso

A Lei Complementar nº 123/2006 manda aplicar ao Simples as regras de juros e multa do imposto de renda. Na prática, valem as regras da Lei nº 9.430/1996:

- **multa de mora de 0,33% por dia** de atraso, contada a partir do dia seguinte ao vencimento, **limitada a 20%**;
- **juros pela taxa Selic** acumulada dos meses entre o vencimento e o pagamento, mais **1% no mês do pagamento**.

Como 20 ÷ 0,33 dá pouco mais de 60, a multa bate no teto de 20% por volta do **61º dia** de atraso. A partir daí ela para de crescer, mas os juros continuam correndo todo mês.

### Exemplo numérico

Uma empresa tinha DAS de **R$ 2.000** com vencimento em 20/10/2026 (terça-feira) e paga em 10/11/2026.

- Dias de atraso: de 21/10 a 10/11 = **21 dias**.
- Multa: 21 × 0,33% = 6,93% de R$ 2.000 = **R$ 138,60**.
- Juros: como o pagamento acontece no mês seguinte ao vencimento, não há mês intermediário de Selic. Entra só o 1% do mês do pagamento = **R$ 20,00**.
- Total: **R$ 2.158,60**.

Se a mesma guia fosse paga só em 21/12/2026, seriam 62 dias de atraso. A multa chegaria ao teto: R$ 400 (20%). Os juros passariam a incluir a Selic de novembro, mais 1% de dezembro.

O sistema faz essas contas sozinho quando você gera a guia na rota certa. O exemplo serve para você entender por que o valor muda a cada dia.

## Erros comuns

1. **Pagar uma guia vencida que estava salva no computador.** O banco pode até aceitar, mas o valor sai sem os acréscimos e sobra diferença em aberto.
2. **Gerar DAS para mês ainda não declarado.** Primeiro transmita o PGDAS-D. Declarar fora do prazo também gera multa própria, de 2% ao mês sobre os tributos declarados, com mínimo de R$ 50 por mês de referência.
3. **Usar o Gerar DAS depois de compensar parte do débito.** A guia vem cheia e você paga em dobro a parte compensada.
4. **Achar que o débito pequeno não tem consequência.** Débito em aberto sem parcelamento é o que leva ao Termo de Exclusão do Simples. Veja [exclusão do Simples por dívida](/blog/exclusao-simples-por-divida-como-regularizar/).

## E quando não dá para pagar tudo?

Se o caixa não comporta pagar à vista, o caminho é o parcelamento em até 60 vezes, com parcela mínima e correção pela Selic. Explicamos as regras em [parcelamento do Simples Nacional](/blog/parcelamento-simples-nacional/). Parcelar cedo costuma sair melhor do que esperar: a multa chega a 20% em cerca de dois meses de qualquer jeito.

## O que fazer agora

1. Entre no PGDAS-D e confira se todos os meses estão declarados.
2. Abra o menu **Débitos** e veja a lista do que está em cobrança.
3. Se algum período aparecer como transferido à PGFN ou ao município, separe esse débito e trate no canal certo.
4. Gere a guia com a data em que o dinheiro vai mesmo sair da conta e pague no mesmo dia.
5. Se a soma for alta, peça ao seu contador a simulação do parcelamento antes de pagar parte e deixar o resto em aberto.
