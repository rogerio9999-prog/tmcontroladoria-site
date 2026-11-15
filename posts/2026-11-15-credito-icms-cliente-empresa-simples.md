---
titulo: "Meu cliente pede crédito de ICMS na nota. Empresa do Simples pode dar?"
resumo: A empresa do Simples pode transferir crédito de ICMS ao cliente que revende ou industrializa, mas só no percentual que ela realmente pagou no DAS. Veja como calcular e o que escrever na nota.
data: 2026-11-15
categoria: Simples Nacional
tags: [Simples Nacional, ICMS, crédito de ICMS, nota fiscal, CSOSN]
fontes:
  - Lei Complementar nº 123/2006, art. 23 | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp123.htm
  - Lei Complementar nº 155/2016 (tabela do Anexo I e repartição do ICMS) | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp155.htm
  - Resolução CGSN nº 140/2018 | http://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=92278
  - Portal Nacional da NF-e | https://www.nfe.fazenda.gov.br/portal/principal.aspx
checagem:
  - Confirmar o número do artigo da Resolução CGSN nº 140/2018 que traz a frase obrigatória sobre o crédito no campo de informações complementares (o texto não cita o artigo)
  - Confirmar se a alíquota informada deve ser arredondada para duas casas decimais (o exemplo usa 2,25%)
  - Confirmar na LC 214/2025 a regra de crédito de CBS e IBS para quem compra de optante do Simples (o texto diz apenas que é, em regra, limitado ao valor pago no DAS)
  - Link do Portal da NF-e não abriu por ferramenta automática (redirecionamento); conferir no navegador
---

A cena é comum para quem vende para outras empresas aqui em Uberaba: o comprador de um supermercado ou de uma indústria pede o orçamento e pergunta "a nota de vocês dá crédito de ICMS?". Se a resposta for "não sei", o fornecedor do Simples sai em desvantagem. A resposta certa é: **dá, dentro de um limite, e desde que a nota seja preenchida do jeito certo**.

## O que a lei permite

A empresa do Simples Nacional não toma crédito nas suas compras e, em regra, não transfere crédito dos tributos pagos no DAS (art. 23 da Lei Complementar nº 123/2006).

A exceção está no **§ 1º do mesmo artigo**: o cliente que **não é do Simples** pode aproveitar crédito de ICMS sobre mercadorias compradas de uma empresa optante, **desde que essas mercadorias sejam destinadas à revenda ou à industrialização**. O crédito é limitado ao ICMS que a empresa do Simples efetivamente devia na operação.

Em outras palavras:

- um atacadista que vai revender o produto pode ter o crédito;
- uma indústria que usa o produto como matéria-prima também;
- um escritório que compra para uso próprio, não;
- um cliente que também é do Simples, não, porque ele não toma crédito nas compras.

## Qual percentual vai na nota

O percentual não é a alíquota cheia do ICMS de Minas Gerais. É a **parcela de ICMS que existe dentro da alíquota do Simples** da empresa vendedora.

Pelo art. 23, § 2º, esse percentual corresponde ao ICMS previsto no Anexo I (comércio) ou no Anexo II (indústria) para a faixa de receita em que a empresa estava **no mês anterior ao da venda**. Na prática, a conta tem dois passos:

1. Calcular a alíquota efetiva do Simples do mês anterior.
2. Multiplicar pelo percentual que o ICMS representa na repartição daquela faixa.

Se a venda acontecer no mês em que a empresa começou a funcionar, usa-se a menor alíquota de ICMS do Anexo I ou II (§ 3º).

## Exemplo com números

Uma distribuidora do Simples faturou **R$ 500 mil nos 12 meses** usados no cálculo do mês anterior (3ª faixa do Anexo I). Ela vende **R$ 10 mil** em mercadorias para um supermercado do Lucro Real, que vai revender.

| Passo | Cálculo | Resultado |
|---|---|---|
| Alíquota efetiva do Simples | (500.000 × 9,5% - 13.860) ÷ 500.000 | 6,728% |
| Parcela do ICMS na 3ª faixa do Anexo I | 33,5% da alíquota efetiva | |
| Percentual de crédito | 6,728% × 33,5% | 2,25% |
| **Crédito para o cliente** | 10.000 × 2,25% | **R$ 225,00** |

Se o mesmo supermercado comprasse de um fornecedor do regime normal, com ICMS de 18%, o crédito seria de R$ 1.800. Essa diferença explica por que alguns compradores pedem desconto a fornecedores do Simples. Saber fazer essa conta ajuda a negociar o preço com números, em vez de ceder no escuro.

## Como fica a nota fiscal

Na NF-e, a venda com direito a crédito sai com o **CSOSN 101** (tributada pelo Simples com permissão de crédito) ou **201** (o mesmo, com cobrança de ICMS por substituição tributária). A NF-e tem campos próprios para o percentual e o valor do crédito. Explicamos todos os códigos em [CSOSN na nota fiscal do Simples](/blog/csosn-nota-fiscal-simples/).

Além disso, a Resolução CGSN nº 140/2018 exige uma frase no campo de informações complementares, informando que a nota **permite o aproveitamento do crédito de ICMS**, com o valor em reais, o percentual e a referência ao art. 23 da LC 123. A maioria dos emissores preenche isso automaticamente quando o CSOSN 101 está configurado com o percentual do mês. O problema é que **o percentual muda todo mês**, junto com o faturamento acumulado, e muita empresa esquece de atualizar o cadastro do emissor.

## Quando não dá crédito

O § 4º do art. 23 lista os casos em que o crédito não se aplica:

- empresa que recolhe ICMS por valor fixo mensal;
- nota sem o percentual de crédito informado;
- isenção do ICMS concedida pelo estado para a faixa de receita da empresa no mês da venda;
- empresa que optou por aplicar a alíquota sobre a receita recebida no mês (regime de caixa), situação que deixa de existir a partir de 2027, quando todas as apurações do Simples passam a ser por competência.

Também não há crédito quando a venda sai sem permissão de crédito (CSOSN 102), por exemplo para consumidor final ou cliente do Simples.

## Erros que geram problema para os dois lados

- **Informar 18% ou 12% como se fosse empresa do regime normal.** O cliente toma crédito a mais e pode ser autuado, e a relação comercial sofre.
- **Usar o percentual de meses atrás.** Se a empresa mudou de faixa, o percentual mudou.
- **Dar crédito em venda para uso e consumo.** O comprador não tem direito, e a nota induz o erro.
- **Esquecer que o crédito acompanha o que foi pago no DAS.** Na revenda de mercadoria que já veio com ICMS retido por substituição tributária (CSOSN 500), a receita sai do cálculo do ICMS no DAS, e não há ICMS próprio para transferir como crédito.

## E com a Reforma Tributária?

O crédito de ICMS continua existindo enquanto o ICMS existir, com redução gradual de 2029 a 2032. A partir de 2027, o cliente também vai olhar para o crédito de CBS, e depois de IBS, que a empresa do Simples transfere em regra limitado ao que pagou no DAS. Para quem vende muito para outras empresas, isso pode justificar a opção pelo regime regular. Tratamos do tema em [prestador de serviço do Simples que vende para empresas](/blog/prestador-servico-simples-b2b-reforma/) e em [Simples Nacional e regime regular de IBS/CBS](/blog/simples-nacional-ibs-cbs-regime-regular/).

## O que fazer agora

1. Separe as vendas para clientes que revendem ou industrializam e confira se as notas saíram com CSOSN 101 ou 201.
2. Peça ao seu contador o percentual de crédito de cada mês e atualize o emissor logo no início do mês.
3. Confira uma nota recente: o percentual, o valor do crédito e a frase nas informações complementares precisam estar lá.
4. Se perde vendas por causa do crédito, faça a conta do custo real para o cliente antes de dar desconto.
