---
titulo: "Errei no PGDAS-D: como retificar a declaração e corrigir o DAS"
resumo: Esqueceu uma nota, marcou o anexo errado ou pagou a mais? Veja como funciona a retificação do PGDAS-D, por que ela mexe nos meses seguintes e quando a correção não entra sozinha no sistema.
data: 2026-11-15
categoria: Simples Nacional
tags: [Simples Nacional, PGDAS-D, retificação, DAS complementar, restituição]
fontes:
  - Manual do PGDAS-D e Defis (versão de 13/11/2026), item 6.10 Retificar Declaração | https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/MANUAL_PGDAS-D_2018_V4.pdf
  - Perguntas e Respostas do Simples Nacional (atualizado em 09/10/2026), perguntas 5.16, 9.16 e capítulo 10 | https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/PerguntaoSN.pdf
  - Lei nº 9.430/1996, art. 61 (multa de mora e juros) | https://www.planalto.gov.br/ccivil_03/leis/l9430.htm
  - Lei Complementar nº 123/2006, arts. 21 e 38-A | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp123.htm
  - gov.br: Solicitar revisão de dívida inscrita (PGFN) | https://www.gov.br/pt-br/servicos/solicitar-revisao-de-divida-inscrita
checagem:
  - Os valores do exemplo são ilustrativos; os juros Selic não foram calculados porque dependem da taxa do período
  - Conferir se a retificação feita depois do início de procedimento de fiscalização perde a espontaneidade e em que termos (o texto só recomenda corrigir antes de qualquer intimação)
  - Conferir se a multa de R$ 20,00 por grupo de dez informações incorretas ou omitidas (art. 38-A da LC 123) pode ser aplicada em retificação espontânea; o texto não afirma que se aplica
  - O manual afirma que retificar a receita de um PA exige retificar as declarações posteriores já transmitidas até dezembro do ano seguinte; conferir se a regra se mantém no manual de 2027
---

Uma nota fiscal ficou de fora do faturamento de agosto. Ou o contador percebeu que os serviços estavam no Anexo IV quando deveriam estar no III. Ou os produtos com substituição tributária foram lançados como receita comum por meses. Todo erro no PGDAS-D tem conserto pelo mesmo caminho: a **declaração retificadora**. O que muda de um caso para outro é o efeito no caixa e o trabalho que vem depois.

## Como retificar

O caminho no PGDAS-D é o mesmo da declaração normal: menu **"Declaração Mensal > Declarar/Retificar"**. Ao informar um período de apuração (PA) já declarado, o sistema pergunta se você quer retificar a declaração anterior. Confirme, corrija o que precisa e clique em "Transmitir".

A retificadora **substitui** a declaração original. Não é um complemento: ela precisa trazer todos os dados do mês, já corrigidos.

## Retificou um mês, os seguintes vêm junto

Esse é o ponto que mais surpreende. A alíquota do Simples depende da RBT12, a soma da receita dos 12 meses anteriores. Se você muda a receita de agosto, muda a RBT12 de setembro, outubro e dos meses seguintes. Por isso o manual do PGDAS-D diz que, ao retificar a receita de um PA, o sistema **exige a retificação das declarações posteriores já transmitidas**, até dezembro do ano seguinte, mesmo que nada mude nelas. É preciso retransmitir para que o cálculo seja refeito.

## Exemplo: a nota esquecida

Uma empresa de serviços de Uberaba, tributada no Anexo III, declarou **R$ 50 mil** em agosto, mas o correto era **R$ 58 mil**. A RBT12 usada em agosto era de R$ 500 mil (3ª faixa: alíquota nominal de 13,5% e parcela a deduzir de R$ 17.640).

- 500.000 × 13,5% = 67.500
- 67.500 - 17.640 = 49.860
- 49.860 ÷ 500.000 = **9,972%**
- Diferença de agosto: 8.000 × 9,972% = **R$ 797,76**

Como o DAS original já foi pago, o sistema gera um **DAS complementar** com a diferença, que vence no prazo original. Pago 30 dias depois do vencimento, ele leva multa de mora de 0,33% por dia (9,9%, ou R$ 78,98), limitada a 20%, mais juros pela taxa Selic.

E setembro? A RBT12 de setembro estava em R$ 520 mil e passa a R$ 528 mil. Com faturamento de R$ 60 mil:

- Antes: (520.000 × 13,5% - 17.640) ÷ 520.000 = 10,108% → R$ 6.064,62
- Depois: (528.000 × 13,5% - 17.640) ÷ 528.000 = 10,159% → R$ 6.095,45

Mais **R$ 30,84** em setembro, e assim por diante nos meses seguintes. Ninguém precisa fazer essa conta à mão, porque o PGDAS-D refaz tudo ao retransmitir. Mas é bom saber que uma nota esquecida tem efeito em cascata.

## O DAS complementar é calculado tributo a tributo

Quando a correção muda a atividade ou o anexo, o resultado pode parecer estranho. O manual do PGDAS-D traz um exemplo: a empresa pagou R$ 773,37 pelo Anexo IV, refez pelo Anexo III e o novo valor deu R$ 970,85. A diferença simples seria R$ 197,48, mas o DAS complementar saiu de **R$ 473,02**.

O motivo: o sistema compara **cada tributo** com o que foi pago. No Anexo III, a contribuição patronal (CPP) entra no DAS, e no Anexo IV ela é paga fora. Faltou CPP, e ela é cobrada inteira. O que foi pago a mais em outros tributos (CSLL, Cofins, ISS) não abate automaticamente: precisa ser pedido de volta.

## Paguei a mais: restituição ou compensação

Se a retificação reduz o imposto de um DAS já pago, sobra crédito. Há dois caminhos no Portal do Simples Nacional:

- **Compensação a Pedido:** usa o crédito para abater débitos do Simples do mesmo tributo e do mesmo ente, vencidos ou a vencer.
- **Pedido Eletrônico de Restituição:** devolve os tributos federais em dinheiro, por PIX. Exige conta gov.br prata ou ouro. ICMS e ISS pagos a mais são pedidos ao estado e ao município.

O prazo é de **5 anos contados do pagamento**, e o valor é corrigido pela Selic.

## Quando a retificação não entra sozinha

Retificar para **aumentar** o imposto é simples. Retificar para **reduzir** pode travar. Segundo o manual, a retificadora que diminui o valor não é carregada automaticamente quando o período está:

- **parcelado:** é preciso pedir a revisão na Receita Federal, comprovando o erro (veja [como funciona o parcelamento do Simples](/blog/parcelamento-simples-nacional/));
- **compensado:** a compensação ativa trava a carga;
- **enviado para dívida ativa:** o pedido de revisão vai para a PGFN (Procuradoria-Geral da Fazenda Nacional), pelo portal Regularize, com cópia da declaração original e da retificadora.

Além disso, retificadoras podem ficar **retidas em malha** para análise da Receita, do estado ou do município. Enquanto estiverem retidas, não produzem efeito. As intimações chegam pela caixa postal do Simples (DTE-SN), e por isso ela precisa ser acompanhada.

## Cuidados antes de retificar

- **Corrija cedo.** Quanto antes, menor a multa de mora no DAS complementar e menor o risco de a correção ser vista como reação a uma fiscalização.
- **Tenha o documento que prova o erro.** Notas, relatórios de vendas, contrato. Retificação para baixo sem prova é o tipo de declaração que cai em malha.
- **Não retifique só o mês do erro.** Retransmita os seguintes, como o sistema pede.
- **Erro de anexo ou de Fator R** muda a CPP e pode gerar complemento alto, como no exemplo. Veja [como o Fator R funciona](/blog/fator-r-simples-nacional/).

## O que fazer agora

1. Compare o faturamento declarado no PGDAS-D com as notas emitidas dos últimos meses. Divergência é o primeiro alvo de malha.
2. Achou erro? Reúna os documentos e peça ao contador a retificação do mês e dos seguintes.
3. Se a correção gerar crédito, decida com o contador entre compensar e restituir, e não deixe passar os 5 anos. Para entender cada tela da apuração, veja o [PGDAS-D passo a passo](/blog/pgdas-d-passo-a-passo-apuracao-mensal/).
