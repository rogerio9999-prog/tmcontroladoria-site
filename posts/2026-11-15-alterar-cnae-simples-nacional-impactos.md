---
titulo: "Vou mudar ou incluir um CNAE na empresa do Simples. O que muda no imposto?"
resumo: Incluir uma atividade no CNPJ pode mudar o anexo, trazer o Fator R para a conta ou até tirar a empresa do Simples. Veja o que conferir antes de alterar o CNAE e um exemplo do impacto no DAS.
data: 2026-11-15
categoria: Simples Nacional
tags: [Simples Nacional, CNAE, alteração contratual, anexos, exclusão do Simples]
fontes:
  - Lei Complementar nº 123/2006, arts. 17, 18, 30 e 31 | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp123.htm
  - Lei Complementar nº 155/2016 (tabelas dos Anexos III e V) | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp155.htm
  - Resolução CGSN nº 140/2018 (Anexo VI, CNAEs impeditivos e ambíguos) | http://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=92278
  - Redesim, registro e alteração de empresas | https://www.gov.br/empresas-e-negocios/pt-br/redesim
  - Portal do Simples Nacional | https://www8.receita.fazenda.gov.br/SimplesNacional/
checagem:
  - Confirmar a forma de comunicar a exclusão obrigatória por atividade vedada no Portal do Simples e se a alteração cadastral com CNAE impeditivo gera exclusão automática
---

"Quero começar a oferecer consultoria, é só incluir o CNAE?" Do ponto de vista do cadastro, quase sempre é simples: uma alteração no contrato social, registrada na Junta Comercial ou no cartório, e o novo código aparece no cartão CNPJ. Do ponto de vista do imposto, a mesma alteração pode deixar o DAS igual, dobrar a alíquota sobre parte da receita ou tirar a empresa do Simples Nacional.

## Primeiro, o que o CNAE é e o que ele não é

CNAE é a Classificação Nacional de Atividades Econômicas, o código que descreve no cadastro o que a empresa faz. Ele serve para a Receita Federal, o estado e o município saberem quais inscrições, licenças e tributos se aplicam.

O que o CNAE **não faz** é definir sozinho quanto a empresa paga no Simples. O anexo é definido pela **receita de cada atividade efetivamente exercida**. Ter um CNAE secundário sem faturar nada nele não muda o DAS. Faturar uma atividade nova sem lançar a receita no anexo certo, sim.

## As quatro perguntas antes de alterar

### 1. A nova atividade é permitida no Simples?

O art. 17 da Lei Complementar nº 123/2006 lista atividades que impedem a opção. A Resolução CGSN nº 140/2018 traz, no Anexo VI, a lista de CNAEs impeditivos e de CNAEs **ambíguos**, que abrangem tanto atividades permitidas quanto vedadas. Explicamos a lista em [atividades impeditivas do Simples Nacional](/blog/atividades-impeditivas-simples-nacional/).

Se a empresa passa a exercer atividade vedada, a exclusão é **obrigatória** (art. 30, II). A comunicação deve ser feita até o último dia útil do mês seguinte ao da situação de vedação, e os efeitos começam no **mês seguinte** ao da ocorrência (art. 31, II). Não é uma exclusão para o ano que vem: é para já.

### 2. Em qual anexo a nova receita vai cair?

Uma empresa que hoje está no Anexo I (comércio) e inclui um serviço passa a ter duas tabelas. Uma empresa de serviços do Anexo III que passa a fazer atividade do Anexo IV começa a recolher a contribuição patronal sobre a folha fora do DAS, ao menos em parte. Veja [Anexo IV e a CPP fora do DAS](/blog/anexo-iv-construcao-civil-cpp-fora-do-das/).

### 3. A nova atividade depende do Fator R?

Consultoria, engenharia, arquitetura, publicidade, tecnologia e outras atividades intelectuais ficam no Anexo III ou no V conforme o **Fator R**: a folha dos últimos 12 meses dividida pelo faturamento dos últimos 12 meses. Com 28% ou mais, Anexo III. Abaixo disso, Anexo V, com alíquota bem mais alta. Detalhes em [Fator R no Simples Nacional](/blog/fator-r-simples-nacional/).

### 4. O que muda nos cadastros do estado e do município?

Incluir comércio pode exigir inscrição estadual na SEF-MG (Secretaria de Estado de Fazenda de Minas Gerais). Incluir serviço pode exigir inscrição municipal e mudar o alvará na Prefeitura de Uberaba. A Redesim integra boa parte desses cadastros, mas cada órgão confere as próprias exigências, e uma licença sanitária ou ambiental pode ser necessária conforme a atividade.

## Exemplo com números

Uma empresa de manutenção de equipamentos (Anexo III) faturou **R$ 300 mil nos últimos 12 meses** (2ª faixa). Ela inclui um CNAE de consultoria técnica e passa a faturar **R$ 30 mil por mês** nessa atividade. A folha da empresa, com pró-labore, fica abaixo de 28% do faturamento, então a consultoria vai para o Anexo V.

| | Anexo III | Anexo V |
|---|---|---|
| Alíquota nominal na 2ª faixa | 11,2% | 18% |
| Parcela a deduzir | R$ 9.360 | R$ 4.500 |
| Alíquota efetiva com RBT12 de R$ 300 mil | 8,08% | 16,50% |
| DAS sobre R$ 30 mil | R$ 2.424 | R$ 4.950 |

Diferença: **R$ 2.526 por mês** sobre a receita de consultoria, ou cerca de **R$ 30.300 por ano**, mantido o mesmo faturamento.

O exemplo simplifica um ponto: a receita nova também aumenta o faturamento acumulado, e com o tempo a empresa pode subir de faixa, o que muda as alíquotas de todas as atividades. Por isso a simulação deve ser feita para os próximos 12 meses, não só para o mês da mudança.

## Cuidados que evitam problema

- **Use o CNAE que descreve a atividade real.** Escolher um código "parecido" para fugir do Anexo V ou de uma vedação não resolve: o que vale é a atividade exercida, e a fiscalização olha contratos e notas.
- **Mantenha o cadastro atualizado.** O oposto também dá problema: a empresa mudou de ramo e o cartão CNPJ continua com a atividade antiga. Isso atrapalha a emissão de notas, a retenção de ISS pelos clientes e o enquadramento.
- **Ajuste o emissor de notas e o PGDAS-D no mesmo mês.** A primeira nota da atividade nova precisa sair com o código de serviço ou o CSOSN certo, e a receita precisa ser lançada separada. Explicamos em [empresa com várias atividades no Simples](/blog/varias-atividades-simples-segregar-anexos/).
- **Confira o objeto social do contrato.** A atividade precisa constar no contrato social, não só no cadastro da Receita.
- **Pense no calendário.** A opção pelo Simples para 2027 já foi encerrada. Se a nova atividade não for permitida no Simples, não há como "esperar janeiro": a exclusão obrigatória vale a partir do mês seguinte.

## O que fazer agora

1. Escreva em uma frase o que a empresa vai passar a fazer e quanto espera faturar com isso.
2. Peça ao seu contador para conferir o CNAE correspondente no Anexo VI da Resolução CGSN nº 140/2018 e o anexo da nova receita.
3. Se a atividade depender do Fator R, simule a folha necessária para ficar no Anexo III antes de começar a faturar.
4. Só então registre a alteração contratual e atualize inscrição estadual, municipal e emissor de notas.
