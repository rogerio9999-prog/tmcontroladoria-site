---
titulo: "CSOSN na nota fiscal do Simples: qual código usar em cada venda"
resumo: O CSOSN diz ao fisco como o ICMS foi tratado em cada item da nota da empresa do Simples. Veja o que significa cada código, os casos mais comuns no comércio e os erros que custam caro.
data: 2026-11-15
categoria: Simples Nacional
tags: [Simples Nacional, CSOSN, NF-e, ICMS, nota fiscal]
fontes:
  - Portal Nacional da NF-e (Manual de Orientação do Contribuinte e notas técnicas) | https://www.nfe.fazenda.gov.br/portal/principal.aspx
  - Lei Complementar nº 123/2006, art. 18, § 4º-A, e art. 23 | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp123.htm
  - Lei Complementar nº 155/2016 (tabela do Anexo I e repartição do ICMS) | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp155.htm
  - Portal do Simples Nacional | https://www8.receita.fazenda.gov.br/SimplesNacional/
checagem:
  - Conferir a descrição oficial de cada CSOSN (101 a 900) na tabela do Manual de Orientação do Contribuinte da NF-e
  - Confirmar a redação da Nota Técnica 2024.001 sobre o CRT 4 para MEI e a data em que passou a valer
  - Link do Portal da NF-e não abriu por ferramenta automática (redirecionamento); conferir no navegador
---

A nota foi rejeitada pela Sefaz, o cliente reclamou que não conseguiu tomar crédito ou, pior, o contador descobriu que a empresa pagou ICMS em dobro sobre produto com substituição tributária. Em boa parte desses casos, o problema está em três ou quatro números na linha do produto: o **CSOSN**.

## O que é o CSOSN

CSOSN significa Código de Situação da Operação no Simples Nacional. É o código que a empresa do Simples informa em cada item da NF-e ou da NFC-e para dizer como o ICMS foi tratado naquela venda.

Empresas do regime normal (Lucro Presumido e Lucro Real) usam outro código, o **CST** (Código de Situação Tributária). Quem diz ao sistema qual dos dois vale é o **CRT**, o Código de Regime Tributário, informado no cabeçalho da nota:

| CRT | Regime do emitente | Código do ICMS nos itens |
|---|---|---|
| 1 | Simples Nacional | CSOSN |
| 2 | Simples Nacional com excesso de sublimite | CST |
| 3 | Regime normal | CST |
| 4 | Simples Nacional, MEI | CSOSN |

O CRT 2 é para a empresa que continua no Simples, mas ultrapassou o sublimite estadual e passou a pagar o ICMS fora do DAS. Explicamos esse caso em [sublimite do Simples Nacional](/blog/sublimite-simples-nacional-icms-iss/). O CRT 4 foi criado pela Nota Técnica 2024.001 para identificar o MEI.

## Os códigos e quando usar

| CSOSN | Significado | Uso típico |
|---|---|---|
| 101 | Tributada pelo Simples **com** permissão de crédito | Venda para cliente que revende ou industrializa |
| 102 | Tributada pelo Simples **sem** permissão de crédito | Venda para consumidor final ou uso e consumo |
| 103 | Isenção do ICMS no Simples para a faixa de receita | Quando o estado concede isenção para a faixa da empresa |
| 201 | Como o 101, com cobrança do ICMS por substituição tributária | A empresa é a substituta e retém o ICMS-ST do cliente |
| 202 | Como o 102, com cobrança do ICMS por substituição tributária | Substituta, venda sem permissão de crédito |
| 203 | Isenção para a faixa de receita, com cobrança por substituição | Raro na prática |
| 300 | Imune | Livros, jornais, papel de impressão, por exemplo |
| 400 | Não tributada pelo Simples | Operações fora do campo do ICMS no Simples, conforme a legislação |
| 500 | ICMS cobrado anteriormente por substituição (substituído) ou por antecipação | Revenda de produto que já chegou com ICMS-ST pago |
| 900 | Outros | Remessas, devoluções e casos que não se encaixam nos anteriores |

No dia a dia de um comércio do Simples, quase tudo cai em **102** e **500**. Indústria e distribuidora que vendem para outras empresas usam muito o **101**.

## O CSOSN e o DAS andam juntos

O CSOSN não muda o imposto sozinho. O que define o DAS é o que a empresa informa no PGDAS-D. Mas os dois precisam contar a mesma história.

O caso clássico é o **500**. A mercadoria chegou com ICMS retido por substituição tributária, então a empresa do Simples não paga de novo o ICMS sobre a revenda. Para isso, a receita precisa ser marcada no PGDAS-D como revenda com substituição tributária (art. 18, § 4º-A, da LC 123). Se a nota sai com CSOSN 500 e o PGDAS-D lança tudo como revenda comum, o ICMS é pago duas vezes.

### Exemplo com números

Uma loja de autopeças do Simples faturou **R$ 500 mil nos últimos 12 meses** (3ª faixa do Anexo I). A alíquota efetiva é:

> (500.000 × 9,5% - 13.860) ÷ 500.000 = **6,728%**

Na 3ª faixa, o ICMS representa **33,5%** dessa alíquota, ou **2,25%** do faturamento. Neste mês, a loja vendeu **R$ 40 mil**, dos quais **R$ 30 mil** em peças com ICMS-ST já pago (CSOSN 500).

- **Lançado corretamente:** sobre os R$ 30 mil, o DAS sai sem a parcela do ICMS. A loja deixa de pagar cerca de 30.000 × 2,25% = **R$ 675** no mês.
- **Lançado errado:** os mesmos R$ 675 são pagos sem necessidade. Em um ano, quase **R$ 8.100**.

Detalhamos a segregação em [receitas monofásicas e com substituição tributária](/blog/monofasico-substituicao-tributaria-simples-segregar-receitas/).

## 101 ou 102: a diferença para o cliente

Com o CSOSN 101, a nota informa o percentual e o valor do crédito de ICMS que o cliente pode aproveitar. Esse percentual muda todo mês, conforme o faturamento acumulado da empresa. Usar 101 com percentual desatualizado ou dar crédito em venda para uso e consumo gera problema para o cliente. O passo a passo está em [crédito de ICMS para cliente de empresa do Simples](/blog/credito-icms-cliente-empresa-simples/).

Com o CSOSN 102, não há crédito. É o código certo para vendas ao consumidor final, inclusive na NFC-e.

## Erros que mais vemos

- **Cadastro de produto feito uma vez e nunca revisado.** O produto passou a ter substituição tributária e o código continua 102.
- **CSOSN 101 para todo mundo.** O emissor vem configurado assim e a empresa dá crédito até para consumidor final.
- **Usar CST quando a empresa é do Simples (ou o contrário).** Normalmente acontece depois de uma mudança de regime, quando o emissor não foi atualizado. A Sefaz rejeita ou, pior, aceita e o erro aparece meses depois.
- **CFOP incoerente com o CSOSN.** Venda de mercadoria com ST usa CFOP próprio, e as duas informações precisam bater.

## E a Reforma Tributária?

A partir de 2027, a NF-e do Simples também passa a ter os campos de CBS e IBS, com códigos próprios de classificação. O CSOSN continua para o ICMS enquanto ele existir. Quem ainda não revisou o cadastro de produtos vai ter dois problemas de uma vez. Veja [cClassTrib e CST no cadastro de produtos](/blog/cclasstrib-cst-nfe-cadastro-produtos/) e [como preparar o emissor de notas para 2027](/blog/preparar-sistema-emissor-nota-2027-reforma/).

## O que fazer agora

1. Exporte do emissor a lista de produtos com NCM, CFOP e CSOSN.
2. Marque quais produtos têm substituição tributária em Minas Gerais e confira se estão com CSOSN 500 na revenda.
3. Confira se o PGDAS-D dos últimos meses separou essas receitas. Se não separou, há valor pago a mais para avaliar com o seu contador.
4. Deixe o CSOSN 101 só para clientes que revendem ou industrializam, com o percentual de crédito atualizado todo mês.
