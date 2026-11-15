---
titulo: "Anexos do Simples Nacional: como descobrir em qual a sua empresa está (e por que isso muda o imposto)"
resumo: O Simples tem cinco tabelas, e a mesma receita pode pagar de 5% a mais de 16% conforme o anexo. Veja como identificar o seu pela atividade e quando o Fator R entra na conta.
data: 2026-11-15
categoria: Simples Nacional
tags: [Simples Nacional, anexos, CNAE, alíquota, Fator R]
fontes:
  - Lei Complementar nº 123/2006, art. 18 e Anexos I a V | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp123.htm
  - Resolução CGSN nº 140/2018 | http://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=92278
  - Portal do Simples Nacional | https://www8.receita.fazenda.gov.br/SimplesNacional/
checagem:
  - Conferir as alíquotas nominais e parcelas a deduzir da 2ª faixa dos Anexos I a V usadas na tabela comparativa (redação da LC 155/2016, sem alteração conhecida para 2026)
  - Confirmar se a LC 227/2026 altera a estrutura dos anexos a partir de 2027 (a mudança conhecida é na partilha, com CBS e IBS no lugar de PIS, Cofins, ICMS e ISS)
---

"Meu vizinho de sala também é do Simples e paga muito menos que eu." Essa frase aparece com frequência aqui no escritório, e quase sempre a explicação é a mesma: as duas empresas estão em **anexos diferentes** do Simples Nacional.

O Simples não tem uma alíquota única. Ele tem cinco tabelas, chamadas de anexos, e cada atividade é tributada por uma delas. Saber em qual a sua empresa está é o primeiro passo para entender o DAS (Documento de Arrecadação do Simples Nacional) que chega todo mês.

## Os cinco anexos em uma frase cada

| Anexo | Para quem | Alíquota inicial |
|---|---|---|
| I | Comércio (lojas, revenda em geral) | 4% |
| II | Indústria (quem fabrica ou transforma) | 4,5% |
| III | Serviços em geral e alguns serviços profissionais com Fator R alto | 6% |
| IV | Construção civil, vigilância, limpeza, advocacia | 4,5% (mas sem INSS patronal dentro do DAS) |
| V | Serviços intelectuais e técnicos com Fator R baixo | 15,5% |

As alíquotas sobem por faixa de faturamento dos últimos 12 meses, até o limite de R$ 4,8 milhões por ano. A lista completa de atividades de cada anexo está no art. 18 da Lei Complementar nº 123/2006.

## Como descobrir o seu anexo, passo a passo

1. **Pegue o cartão CNPJ** no site da Receita Federal e veja a atividade principal e as secundárias (os códigos CNAE, a Classificação Nacional de Atividades Econômicas).
2. **Separe o que você realmente fatura.** O anexo é definido pela receita de cada atividade exercida, e não só pelo CNAE principal. Uma loja que também faz instalação tem receita de comércio (Anexo I) e de serviço (Anexo III ou outro).
3. **Confira a regra da atividade na LC 123.** Alguns serviços têm anexo fixo. Outros dependem do **Fator R**, que é a folha de salários dividida pelo faturamento.
4. **Veja como o DAS está sendo gerado.** No PGDAS-D, o sistema de cálculo do Simples, cada receita é informada por tipo. Um erro de marcação ali faz a empresa pagar pelo anexo errado, para mais ou para menos.

## O peso da escolha: a mesma receita em cada anexo

Para mostrar o tamanho da diferença, imagine uma empresa com **R$ 300 mil de faturamento nos últimos 12 meses** (2ª faixa de todas as tabelas). A alíquota efetiva é calculada assim:

> (faturamento de 12 meses × alíquota nominal - parcela a deduzir) ÷ faturamento de 12 meses

| Anexo | Alíquota nominal | Parcela a deduzir | Alíquota efetiva |
|---|---|---|---|
| I | 7,3% | R$ 5.940 | 5,32% |
| II | 7,8% | R$ 5.940 | 5,82% |
| III | 11,2% | R$ 9.360 | 8,08% |
| IV | 9% | R$ 8.100 | 6,30% |
| V | 18% | R$ 4.500 | 16,50% |

No Anexo III, um mês de R$ 25 mil de faturamento geraria DAS de cerca de R$ 2.020. No Anexo V, de R$ 4.125. É dinheiro que se repete todo mês.

Um detalhe sobre o Anexo IV: a alíquota parece baixa, mas a empresa paga **à parte** a contribuição previdenciária patronal sobre a folha (20% mais os adicionais). Quem compara só a tabela se engana.

## O Fator R e a ponte entre os Anexos III e V

Para várias atividades intelectuais (consultoria, engenharia, arquitetura, medicina, tecnologia, publicidade e outras), o anexo não é fixo. Se a folha dos últimos 12 meses, incluindo pró-labore, for **igual ou maior que 28% do faturamento**, a tributação é pelo Anexo III. Se for menor, pelo Anexo V.

O cálculo é refeito todo mês. Explicamos a conta completa, com exemplo, no artigo sobre [Fator R](/blog/fator-r-simples-nacional/).

## Erros mais comuns que vemos

- **CNAE desatualizado.** A empresa mudou de ramo e o cadastro continua com a atividade antiga. Isso pode até levar a um anexo mais caro ou a uma atividade que não pode estar no Simples.
- **Tudo marcado como uma atividade só.** Comércio e serviço misturados no mesmo campo do PGDAS-D.
- **Esquecer a revenda com substituição tributária ou produtos monofásicos.** Elas continuam no Anexo I, mas com parte dos tributos excluída do cálculo. É um tema à parte, que tratamos em [como segregar receitas monofásicas e com substituição tributária](/blog/monofasico-substituicao-tributaria-simples-segregar-receitas/).
- **Achar que o anexo é escolha.** Não é. A lei define. O que a empresa pode fazer é organizar a operação (folha, contratos, separação de atividades) dentro das regras.

## E a Reforma Tributária?

A partir de 2027, a parte do DAS que hoje corresponde a PIS e Cofins dá lugar à CBS, e mais adiante ICMS e ISS darão lugar ao IBS. A lógica dos anexos por atividade continua, mas a divisão interna de cada alíquota muda. Quem vende para outras empresas também vai precisar olhar a opção pelo regime regular de IBS e CBS. Tratamos disso em [Simples Nacional e regime regular de IBS/CBS](/blog/simples-nacional-ibs-cbs-regime-regular/).

## O que fazer agora

1. Baixe o cartão CNPJ e liste todas as atividades que a empresa exerce de fato.
2. Peça ao seu contador o extrato do PGDAS-D dos últimos meses e confira em qual anexo cada receita foi informada.
3. Se a empresa presta serviços intelectuais, calcule o Fator R dos últimos 12 meses.
4. Se encontrar divergência, não retifique sozinho: um contador avalia se há valor pago a mais para recuperar ou diferença a regularizar.
