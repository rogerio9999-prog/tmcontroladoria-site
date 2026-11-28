---
titulo: "Simulação de margem para 2027: como testar três cenários de alíquota antes de mexer na tabela de preços"
resumo: Ninguém sabe ainda a alíquota final. Em vez de esperar, monte três cenários numa planilha e veja o que acontece com o preço ao cliente, o imposto a recolher e o crédito das compras. Exemplo com números fictícios.
data: 2026-11-28
categoria: Reforma Tributária
tags: [reforma tributária, simulação, margem, precificação, crédito, IBS, CBS]
fontes:
  - Lei Complementar nº 214/2025, texto compilado | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214compilado.htm
  - Emenda Constitucional nº 132/2023 | https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc132.htm
  - Receita Federal, Reforma Tributária do Consumo | https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/acoes-e-programas/programas-e-atividades/reforma-tributaria-do-consumo/entenda
checagem:
  - As alíquotas de 20%, 26% e 30% e o crédito reduzido de 5% do exemplo são FICTÍCIOS, só para ilustrar o raciocínio; confirmar que o texto deixa isso claro em todas as menções
  - Confirmar que o modelo simplificado (imposto por fora, débito sobre a venda menos crédito sobre a compra, sem outras particularidades como redutores, regimes específicos e transição gradual) não induz o leitor a erro
  - Os links de fontes não puderam ser abertos durante a redação (rede do ambiente restrita); conferir antes de aprovar
---

"Qual será a alíquota?" é a pergunta que trava muita tabela de preços em 2026. A resposta honesta é que o número final ainda depende de decisões que não saíram. Esperar, porém, não ajuda quem vende em janeiro. A saída é **simular**: montar cenários, ver o que muda em cada um e saber de antemão onde o seu negócio é sensível.

Os números abaixo são **fictícios**. Servem para mostrar o método, não para prever alíquota.

## O modelo simples

Para a empresa no regime regular, a lógica do novo imposto é esta:

- o imposto é **somado por fora** ao preço (veja [precificação com IBS e CBS](/blog/precificacao-ibs-cbs-preco-por-fora/));
- o que você recolhe é o **imposto da venda menos o imposto das compras** que dão crédito;
- o cliente final paga o preço mais o imposto.

Quem está no Simples tem regras próprias. Para esse caso, comece por [Simples Nacional e a Reforma Tributária](/blog/simples-nacional-ibs-cbs-regime-regular/).

## O exemplo: uma loja que revende

Uma loja de Uberaba compra um produto por **R$ 600,00** (valor sem imposto) e quer vender por **R$ 1.000,00** (também sem imposto). Isso já embute despesas e margem. Vamos testar três alíquotas totais fictícias:

| Cenário | Alíquota fictícia | Imposto na venda | Crédito na compra (integral) | Imposto a recolher | Preço pago pelo cliente |
|---|---|---|---|---|---|
| A | 20% | R$ 200,00 | R$ 120,00 | R$ 80,00 | R$ 1.200,00 |
| B | 26% | R$ 260,00 | R$ 156,00 | R$ 104,00 | R$ 1.260,00 |
| C | 30% | R$ 300,00 | R$ 180,00 | R$ 120,00 | R$ 1.300,00 |

Duas leituras importantes:

1. **O imposto a recolher cresce menos do que o preço final.** Quem repassa o imposto por fora, com crédito integral, não perde margem. O que muda é o que o **cliente** paga.
2. **O seu risco está no preço percebido.** Se o concorrente vende com o mesmo imposto, a comparação continua justa. Se o concorrente está num regime diferente, a comparação pode mudar.

## O segundo teste: e se o crédito for menor?

Agora suponha que o fornecedor da loja seja do Simples e gere, fictícia e hipoteticamente, um crédito de só **5%** do valor da compra. Com a alíquota de 26%:

- Imposto na venda: R$ 260,00
- Crédito: 5% de R$ 600,00 = R$ 30,00
- **Imposto a recolher: R$ 230,00**, contra R$ 104,00 com crédito integral

A diferença é de **R$ 126,00 por unidade**. Se a loja não repassar, a margem some. Se repassar, o preço ao cliente sobe. Por isso vale comparar fornecedores antes de renovar contratos. Há um exemplo completo em [Simples ou regime regular: como comparar o custo real da compra](/blog/comparar-fornecedor-simples-regime-regular-2027/).

## Como montar a sua planilha

Faça uma aba por produto ou serviço principal, com as colunas:

1. Custo de compra sem imposto
2. Preço de venda desejado sem imposto
3. Alíquota do cenário (três linhas: baixa, média e alta)
4. Crédito da compra (integral e reduzido)
5. Imposto a recolher
6. Preço final ao cliente
7. Margem em reais e em percentual

Depois olhe os **itens mais sensíveis**: os que têm pouca margem e muita compra de fornecedor sem crédito pleno. São eles que pedem atenção primeiro.

## O que esta simulação não captura

- Redução de alíquota para alguns setores e itens, que muda o cenário de quem é beneficiado. Veja [redução de 60% para setores](/blog/reducao-60-por-cento-ibs-cbs-setores/).
- A transição gradual entre os impostos atuais e os novos, que não acontece de uma vez. O [cronograma até 2033](/blog/cronograma-reforma-tributaria-2026-2033/) mostra as fases.
- Particularidades de cada produto ou serviço. Quem classifica o item é o cadastro fiscal, e o seu contador deve revisar.

## Exemplo de leitura dos resultados

Voltando à loja: no cenário B, com crédito integral, o imposto a recolher por unidade é R$ 104,00 e o cliente paga R$ 1.260,00. Se a loja vende 200 unidades por mês, o imposto líquido recolhido seria R$ 20.800,00 (104 × 200). No cenário com crédito reduzido, seria R$ 46.000,00 (230 × 200). A diferença mensal, R$ 25.200,00, é o tamanho do problema que a escolha do fornecedor pode criar ou resolver. Os valores são fictícios, mas a ordem de grandeza mostra por que a simulação vale uma tarde de trabalho.

## O que fazer agora

- Escolha os cinco produtos ou serviços que mais pesam no seu faturamento.
- Monte a planilha com três cenários e dois níveis de crédito.
- Liste os fornecedores de cada um e pergunte qual regime eles estão.
- Leve os resultados ao seu contador antes de fechar a tabela de 2027. A decisão do seu caso depende do seu regime e das suas compras.
