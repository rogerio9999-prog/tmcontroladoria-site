---
titulo: "Retenção de ISS na empresa do Simples Nacional: qual alíquota informar na nota e como não pagar duas vezes"
resumo: Quando o cliente retém o ISS, a empresa do Simples deve informar na nota a alíquota efetiva de ISS do mês anterior e excluir esse valor do DAS. Veja o cálculo com exemplo e os erros mais comuns.
data: 2026-11-15
categoria: Simples Nacional
tags: [Simples Nacional, ISS, retenção, NFS-e, prestador de serviços]
fontes:
  - Lei Complementar nº 123/2006, art. 21, § 4º | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp123.htm
  - Resolução CGSN nº 140/2018 (retenção do ISS) | http://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=92278
  - Lei Complementar nº 116/2003 (ISS) | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp116.htm
  - Portal Nacional da NFS-e | https://www.gov.br/nfse/pt-br
checagem:
  - Conferir a partilha do ISS na 3ª faixa do Anexo III (32,5%) usada no exemplo
  - Confirmar que a retenção de ISS não se aplica a serviços prestados por MEI
  - Confirmar as hipóteses em que a Prefeitura de Uberaba atribui responsabilidade pela retenção ao tomador (legislação municipal)
  - Confirmar a regra de que, quando a alíquota efetiva de ISS ultrapassa 5%, a diferença é tratada de forma específica no Anexo III, 5ª faixa
---

O cliente pagou a nota de R$ 10 mil, mas depositou só R$ 9.680,69. Ligou o financeiro e explicou: "retivemos o ISS". Para a empresa do Simples Nacional, isso levanta duas perguntas. Qual era o valor certo a ser retido? E como evitar pagar esse mesmo ISS de novo dentro do DAS?

## Quando o ISS é retido

O ISS (Imposto Sobre Serviços) é um imposto municipal. Em regra, quem recolhe é o prestador. Mas a Lei Complementar nº 116/2003 e as leis de cada município podem obrigar o **tomador** (o cliente) a reter e recolher o imposto no lugar do prestador. É comum em contratos com empresas maiores, órgãos públicos e em certos serviços, como construção civil, limpeza, vigilância e serviços prestados fora do município do prestador.

A empresa do Simples não fica fora disso. O que muda é **qual alíquota** o cliente deve reter.

## A alíquota que vale para a empresa do Simples

A Lei Complementar nº 123/2006 (art. 21, § 4º) define que a retenção deve usar a **alíquota efetiva de ISS** da empresa do Simples, e não a alíquota cheia do município:

- A alíquota a ser informada na nota é a **alíquota efetiva de ISS do mês anterior** ao da prestação.
- Se a empresa está no **primeiro mês de atividade**, a alíquota é de **2%**.
- Se a empresa **não informar** a alíquota na nota, o tomador aplica **5%**.

Ou seja: deixar o campo em branco faz a empresa perder dinheiro.

## Como achar a alíquota efetiva de ISS

A alíquota efetiva de ISS é a parte do DAS que corresponde ao ISS. Ela sai de duas contas:

1. **Alíquota efetiva total** do mês, pela fórmula do Simples.
2. **Percentual de ISS** na partilha do anexo e da faixa.

**Exemplo:** uma empresa de manutenção de equipamentos (Anexo III) com RBT12 de **R$ 480 mil** está na 3ª faixa (13,5% e parcela a deduzir de R$ 17.640). O ISS representa 32,5% do DAS nessa faixa.

- Alíquota efetiva total: (480.000 × 13,5% - 17.640) ÷ 480.000 = **9,825%**
- Alíquota efetiva de ISS: 9,825% × 32,5% = **3,19%**

Em uma nota de **R$ 10.000** para um cliente que retém o ISS:

| | Valor |
|---|---|
| ISS retido pelo cliente (3,19%) | R$ 319,31 |
| DAS sobre a nota sem retenção (9,825%) | R$ 982,50 |
| DAS sobre a nota com retenção (sem a parte do ISS) | **R$ 663,19** |
| Total pago (retenção + DAS) | R$ 982,50 |

A empresa paga, no total, o mesmo que pagaria sem retenção. Só que parte vai pelo cliente e parte pelo DAS.

## O erro que faz pagar duas vezes

No PGDAS-D, a receita da nota com ISS retido deve ser informada como **"com retenção/substituição tributária de ISS"**. Assim, o sistema tira a parcela de ISS do cálculo. Se a empresa informar como receita comum, paga o ISS **duas vezes**: uma pela retenção do cliente, outra dentro do DAS. No exemplo acima, seriam R$ 319,31 a mais por nota.

Outros erros comuns:

- **Não informar a alíquota na nota**, e o cliente reter 5% em vez de 3,19%.
- **Informar a alíquota total do DAS** (9,825%) como se fosse ISS.
- **Usar a alíquota de meses atrás.** Ela muda conforme o RBT12 e precisa ser atualizada todo mês.
- **Não conferir se o cliente recolheu.** O ISS retido e não recolhido é problema do tomador perante a prefeitura, mas pode atrapalhar certidões do prestador.

## E o MEI?

O MEI paga ISS em valor fixo dentro do DAS-MEI e, em regra, não sofre retenção. Se um cliente insistir em reter, mostre o enquadramento no cartão CNPJ e no Portal do Simples. Veja também [nota fiscal de serviço do MEI](/blog/mei-nota-fiscal-servico-padrao-nacional/).

## A NFS-e nacional e a reforma

A NFS-e em padrão nacional, emitida pelo Emissor Nacional ou pelos sistemas municipais integrados, já tem campo próprio para a retenção. E, com a Reforma Tributária, o ISS será substituído pelo IBS entre 2029 e 2032. Até lá, a lógica da retenção continua valendo. Para quem presta serviço a outras empresas, a reforma traz outra decisão importante, que tratamos em [prestador de serviço do Simples no B2B](/blog/prestador-servico-simples-b2b-reforma/).

## O que fazer agora

1. Peça ao contador a alíquota efetiva de ISS de cada mês, junto com a guia do DAS.
2. Configure o emissor de NFS-e para informar essa alíquota nas notas com retenção.
3. Confira, no PGDAS-D dos últimos meses, se as notas com retenção foram marcadas corretamente.
4. Se houve pagamento em duplicidade, avalie com o contador a retificação e a recuperação dos valores.
