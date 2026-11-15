---
titulo: "Como preparar o sistema emissor de notas para 2027: checklist da Reforma Tributária"
resumo: Em janeiro de 2027, a CBS passa a valer de verdade e o Simples começa a informar IBS e CBS na nota. Veja um checklist prático para revisar o emissor, o cadastro e os relatórios antes da virada do ano.
data: 2026-11-15
categoria: Reforma Tributária
tags: [NF-e, NFC-e, NFS-e, sistema emissor, 2027, checklist, Simples Nacional]
fontes:
  - Portal Nacional da NF-e (notas técnicas da Reforma Tributária) | https://www.nfe.fazenda.gov.br/portal/principal.aspx
  - Ministério da Fazenda, regulamento da CBS e do IBS | https://www.gov.br/fazenda/pt-br/assuntos/noticias/2026/abril/regulamento-detalha-as-regras-que-apresentam-sistema-mais-simples-transparente-e-previsivel-para-cidadaos-e-empresas
  - Lei Complementar nº 214/2025, texto compilado | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214compilado.htm
  - Portal da NFS-e Padrão Nacional | https://www.gov.br/nfse/pt-br
checagem:
  - Confirmar a data de exigência dos campos de IBS e CBS em produção para optantes do Simples (CRT 1) e MEI (CRT 4); fontes de mercado citam 04/01/2027 com base na NT 2025.002 e a NT 2026.005 (30/10/2026) trouxe os campos próprios do Simples
  - Confirmar a situação de Uberaba em relação à NFS-e padrão nacional antes de citar a cidade de forma específica
  - A alíquota cheia de 26% do exemplo é HIPOTÉTICA
  - Confirmar que o link do Portal da NFS-e (gov.br/nfse) abre e trata do padrão nacional
  - O link do Portal Nacional da NF-e entrou em loop de redirecionamento na verificação automática; confirmar no navegador que abre (detalhe menor)
---

Na primeira semana de janeiro, o seu emissor de notas vai precisar estar pronto para um cenário novo: PIS e Cofins extintos, CBS cobrada de verdade, IBS ainda simbólico e, para quem é do Simples Nacional, campos de IBS e CBS na nota pela primeira vez. Descobrir um problema de sistema no dia 4 de janeiro, com o caixa aberto e o cliente esperando a nota, é a pior forma de começar 2027.

## O que muda na nota em 2027

- **Empresas do Lucro Presumido e do Real** já informam CBS e IBS desde agosto de 2026, no ano teste. Em 2027, os valores deixam de ser simbólicos para a CBS, e os campos de PIS e Cofins perdem a função para fatos geradores novos.
- **Optantes do Simples e MEI** ficaram dispensados em 2026. As notas técnicas preveem a exigência dos campos de IBS e CBS para eles a partir do início de janeiro de 2027, com regras próprias publicadas em outubro de 2026.
- **Imposto Seletivo** entra para fabricantes e importadores de itens como bebidas, veículos e cigarros. Veja [Imposto Seletivo: o que é e quem paga](/blog/imposto-seletivo-o-que-e-quem-paga/).

## Checklist do sistema

**1. Versão do emissor**
- O fornecedor já liberou a versão que atende às notas técnicas mais recentes da NF-e e NFC-e?
- Se você usa emissor gratuito ou da prefeitura, ele já foi atualizado?

**2. Cadastro de produtos e serviços**
- Todo item tem NCM correto?
- Todo item tem CST e cClassTrib de IBS e CBS? Veja [cClassTrib e CST na NF-e](/blog/cclasstrib-cst-nfe-cadastro-produtos/).
- Os itens com alíquota zero ou redução de 60% estão marcados como tal?

**3. Cadastro de clientes**
- O sistema identifica se o cliente é contribuinte do regime regular, do Simples ou consumidor final?
- O CPF do consumidor é registrado com facilidade no caixa?

**4. Operações especiais**
- Devoluções, bonificações, brindes, remessas para conserto e consignação estão parametrizadas?
- Vendas para órgãos públicos têm tratamento próprio?

**5. Relatórios**
- O sistema gera relatório de débitos de CBS e IBS por período?
- Ele registra os créditos das notas de compra, separados por tributo?

**6. Testes**
- Emitir notas de teste em homologação para cada tipo de operação.
- Conferir os valores com o contador antes de liberar em produção.

## Serviços: a NFS-e

Quem presta serviço emite NFS-e, a nota de serviço. Com a Reforma, ganhou força a NFS-e no padrão nacional, que já traz os campos de IBS e CBS. Confirme com a prefeitura do seu município e com o seu contador qual emissor usar em 2027 e se o código do serviço está correto.

## Exemplo: o custo de um item mal cadastrado

Uma loja de produtos naturais em Uberaba, fora do Simples, vende R$ 15.000 por mês de um item que tem direito à redução de 60%, mas ele ficou cadastrado como tributação integral. Usando uma **alíquota cheia hipotética de 26%**:

| Cenário | Cálculo | IBS e CBS no mês |
|---|---|---|
| Cadastro errado (integral) | R$ 15.000 × 26% | R$ 3.900 |
| Cadastro certo (redução de 60%) | R$ 15.000 × 26% × 40% | R$ 1.560 |
| **Diferença por mês** | | **R$ 2.340** |
| Diferença em 12 meses | R$ 2.340 × 12 | R$ 28.080 |

E esse é um único produto. Agora pense no tempo de revisão: um cadastro de 400 itens, a 3 minutos por item, leva cerca de 20 horas de trabalho. É bem mais barato gastar essas horas em dezembro.

## Quem faz o quê

| Tarefa | Responsável |
|---|---|
| Atualizar a versão do sistema | Fornecedor do software |
| Revisar NCM, CST e cClassTrib | Empresa, com validação do contador |
| Testar notas em homologação | Empresa e fornecedor |
| Validar valores e relatórios | Contador |
| Treinar caixa e faturamento | Empresa |

## O que fazer agora

1. **Ligue hoje para o fornecedor do sistema** e pergunte, por escrito, quando sai a versão para 2027 e o que ela cobre.
2. **Comece a revisão do cadastro** pelos itens de maior faturamento.
3. **Marque uma data em dezembro** para emitir notas de teste e revisar com o contador.
4. **Treine quem emite nota**, principalmente para devoluções e operações fora do padrão.
5. **Se for do Simples**, veja também se o DAS continua sendo a melhor opção em [Simples Nacional na Reforma: continuar no DAS ou recolher IBS e CBS por fora?](/blog/simples-nacional-ibs-cbs-regime-regular/).
