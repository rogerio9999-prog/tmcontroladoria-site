---
titulo: "Empresa com várias atividades no Simples: como separar as receitas entre os anexos"
resumo: Quem vende produto e presta serviço no mesmo CNPJ paga cada receita pela tabela do seu anexo, mas todas usam o mesmo faturamento de 12 meses. Veja o cálculo e os erros mais comuns.
data: 2026-11-15
categoria: Simples Nacional
tags: [Simples Nacional, segregação de receitas, anexos, PGDAS-D, DAS]
fontes:
  - Lei Complementar nº 123/2006, art. 18, §§ 1º, 1º-A, 4º e 4º-A | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp123.htm
  - Lei Complementar nº 155/2016 (tabelas dos Anexos I a V) | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp155.htm
  - Resolução CGSN nº 140/2018 | http://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=92278
  - Portal do Simples Nacional | https://www8.receita.fazenda.gov.br/SimplesNacional/
checagem:
  - Confirmar na Resolução CGSN nº 140/2018 que, em empresa com atividades mistas, o Fator R considera a folha total e a receita bruta total da empresa
---

Uma loja de ar-condicionado vende o aparelho e cobra pela instalação. Uma oficina vende a peça e cobra a mão de obra. Uma gráfica imprime e também faz criação de arte. Nos três casos, o mesmo CNPJ tem receitas que a lei manda tributar por **anexos diferentes** do Simples Nacional. Se tudo for informado como uma coisa só, o DAS sai errado, para mais ou para menos.

## A regra em duas frases

1. **Cada receita é tributada pela tabela do anexo da sua atividade.** O art. 18, § 4º, da Lei Complementar nº 123/2006 manda a empresa destacar separadamente a revenda de mercadorias, a venda de produtos que ela fabrica, a prestação de serviços e a locação de bens móveis.
2. **A faixa de todas as tabelas é definida pelo faturamento total da empresa.** A receita bruta dos últimos 12 meses (RBT12) é uma só, somando todas as atividades. Ela é usada para calcular a alíquota efetiva de cada anexo.

Não existe "um faturamento para o comércio e outro para o serviço". Existe um faturamento total, aplicado a tabelas diferentes.

## Exemplo com números

Uma empresa do Triângulo Mineiro vende e instala equipamentos. Nos últimos 12 meses, faturou **R$ 420 mil** no total (3ª faixa). Neste mês:

- venda de equipamentos (revenda, Anexo I): **R$ 25 mil**
- instalação (serviço, Anexo III): **R$ 10 mil**

A fórmula da alíquota efetiva (art. 18, § 1º-A) é:

> (RBT12 × alíquota nominal - parcela a deduzir) ÷ RBT12

| | Anexo I (revenda) | Anexo III (instalação) |
|---|---|---|
| Alíquota nominal na 3ª faixa | 9,5% | 13,5% |
| Parcela a deduzir | R$ 13.860 | R$ 17.640 |
| Alíquota efetiva com RBT12 de R$ 420 mil | 6,20% | 9,30% |
| Receita do mês | R$ 25.000 | R$ 10.000 |
| **DAS de cada parcela** | **R$ 1.550** | **R$ 930** |

**DAS correto do mês: R$ 2.480.**

Agora os dois erros comuns:

- **Tudo informado como serviço:** 35.000 × 9,30% = R$ 3.255. A empresa paga **R$ 775 a mais** no mês.
- **Tudo informado como revenda:** 35.000 × 6,20% = R$ 2.170. A empresa paga **R$ 310 a menos** e fica exposta a cobrança da diferença, com multa e juros. Além disso, o ICMS e o ISS do DAS ficam com os entes errados: o estado recebe pelo que deveria ter ido para o município.

## Onde a separação acontece na prática

A separação é feita no **PGDAS-D**, o sistema em que a empresa declara a receita e gera o DAS. Para cada estabelecimento, a receita é lançada por tipo de atividade, e o sistema aplica o anexo correspondente. O PGDAS-D não adivinha nada: ele calcula a partir do que foi marcado.

Por isso, a separação começa antes, na **nota fiscal**:

- venda de mercadoria sai em NF-e (ou NFC-e), com o CSOSN correto (veja [CSOSN na nota fiscal do Simples](/blog/csosn-nota-fiscal-simples/));
- serviço sai em NFS-e;
- se o sistema permitir nota conjugada, os valores de produto e serviço precisam estar separados no documento.

Quando a loja cobra "aparelho instalado" por um preço fechado e emite só uma nota de venda, a empresa perde a prova de quanto era serviço. Na fiscalização, isso vira discussão.

## Separações dentro da mesma atividade

Além de separar comércio, indústria e serviço, o art. 18, § 4º-A, exige destacar dentro de cada atividade:

- receitas com **produtos monofásicos** ou com **substituição tributária** do ICMS, em que parte dos tributos já foi paga antes. Detalhamos em [como segregar receitas monofásicas e com substituição tributária](/blog/monofasico-substituicao-tributaria-simples-segregar-receitas/);
- serviços com **ISS retido** pelo tomador;
- receitas de **exportação**;
- receitas com isenção, redução ou valor fixo.

Cada marcação errada é dinheiro pago a mais ou a menos.

## Serviços: Anexo III, IV ou V no mesmo CNPJ

Serviço não é tudo igual. Uma empresa pode ter, por exemplo, manutenção (Anexo III), projetos de engenharia (Anexo III ou V, conforme o Fator R) e execução de obra (Anexo IV). Cada receita vai para o seu anexo.

Quando há atividades sujeitas ao Fator R, a relação entre folha e faturamento é apurada para a empresa como um todo. Se o resultado for 28% ou mais, as atividades sujeitas ao Fator R vão para o Anexo III; abaixo disso, para o V. As demais atividades não mudam de anexo. A conta completa está em [Fator R no Simples Nacional](/blog/fator-r-simples-nacional/).

Se uma das atividades for do Anexo IV, a contribuição patronal sobre a folha tem tratamento próprio, fora do DAS. Explicamos em [Anexo IV e a CPP fora do DAS](/blog/anexo-iv-construcao-civil-cpp-fora-do-das/).

## Sinais de que a sua empresa pode estar errando

- O DAS sai todo mês em um anexo só, mas a empresa emite NF-e e NFS-e.
- O preço de venda inclui serviço, mas a nota é só de mercadoria (ou só de serviço).
- A empresa começou uma atividade nova e ninguém mudou a forma de lançar no PGDAS-D.
- O CNAE secundário existe no cartão CNPJ, mas a receita dele nunca aparece na declaração.

## E a partir de 2027?

Com a Reforma Tributária, a parte do DAS que hoje é PIS e Cofins passa a ser CBS, e depois o ICMS e o ISS dão lugar ao IBS. A lógica de separar a receita por atividade continua. Quem vende para outras empresas pode ainda avaliar o regime regular de CBS e IBS, tema de [Simples Nacional e regime regular de IBS/CBS](/blog/simples-nacional-ibs-cbs-regime-regular/).

## O que fazer agora

1. Liste todas as atividades que a empresa exerce de fato e o anexo de cada uma.
2. Compare as notas emitidas no mês (NF-e e NFS-e) com o que foi informado no PGDAS-D, atividade por atividade.
3. Se vende produto com serviço incluso, defina com o seu contador como separar o preço nas notas a partir de agora.
4. Se encontrar meses lançados errado, não refaça por conta própria: a retificação pode gerar valor a recuperar ou diferença a pagar, e as duas coisas precisam ser tratadas juntas.
