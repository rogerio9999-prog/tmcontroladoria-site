---
titulo: "EFD-Reinf: o que é, quem precisa entregar e qual o prazo"
resumo: A EFD-Reinf reúne as retenções e informações fiscais que não estão no eSocial: INSS retido em serviços, IR retido de terceiros e, desde 2026, informações de lucros e dividendos. Veja quem entrega e quando.
data: 2026-11-15
categoria: Trabalhista e Folha
tags: [EFD-Reinf, retenções, DCTFWeb, IRRF, obrigações acessórias]
fontes:
  - SPED, Receita Federal: EFD-Reinf (manuais e leiautes) | http://sped.rfb.gov.br/pasta/show/2225
  - Declarar Débitos e Créditos Tributários Federais (DCTFWeb), gov.br | https://www.gov.br/pt-br/servicos/declarar-debitos-e-creditos-tributarios-federais
  - Lei nº 8.212/1991, art. 31 (retenção de 11% na cessão de mão de obra) | https://www.planalto.gov.br/ccivil_03/leis/l8212cons.htm
  - Lei nº 15.270/2025 (tributação de lucros e dividendos) | https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15270.htm
checagem:
  - Confirmar que o link do portal SPED (sped.rfb.gov.br) está acessível; na revisão ele não abriu
  - Confirmar na IN RFB 2.043/2021 (redação da IN 2.163/2023) que o prazo do dia 15 é postergado para o primeiro dia útil seguinte, e que a competência outubro/2026 vence em 16/11/2026
  - Confirmar os eventos e prazos da EFD-Reinf para informar lucros e dividendos em 2026
---

Muita empresa pequena descobre a EFD-Reinf do pior jeito: a DCTFWeb não fecha, a certidão negativa trava ou chega uma multa por atraso de uma declaração que ninguém sabia que precisava entregar. A Reinf não é exclusividade de empresa grande. Basta contratar um serviço com retenção ou pagar um aluguel a uma pessoa física para ela entrar na rotina.

## O que é a EFD-Reinf

É a **Escrituração Fiscal Digital de Retenções e Outras Informações Fiscais**, um módulo do SPED da Receita Federal. Ela complementa o eSocial:

- o **eSocial** traz tudo o que é relacionado a trabalhadores (folha, pró-labore, afastamentos);
- a **EFD-Reinf** traz o que **não é folha**: retenções sobre serviços, pagamentos a terceiros, receitas específicas.

Os dois alimentam a **DCTFWeb**, que gera o DARF. Se a Reinf não for fechada, a DCTFWeb fica incompleta. Veja como as três se conectam em [DCTFWeb: o que é e qual o prazo](/blog/dctfweb-o-que-e-prazo/).

## O que vai na EFD-Reinf

Os eventos são organizados em séries:

| Série | O que informa | Exemplo prático |
|---|---|---|
| R-1000 | Cadastro do contribuinte | Primeiro envio |
| R-2010 | Serviços **tomados** com cessão de mão de obra ou empreitada (INSS retido de 11%) | Empresa que contrata limpeza ou vigilância terceirizada |
| R-2020 | Serviços **prestados** com essa retenção | Empresa de limpeza que teve 11% retidos pelo cliente |
| R-2055 | Aquisição de produção rural | Frigorífico ou cerealista que compra de produtor |
| R-2060 | Contribuição previdenciária sobre a receita bruta (CPRB) | Empresas da desoneração da folha |
| R-4010 | Pagamentos e retenções a **pessoas físicas** | Aluguel pago a pessoa física, serviços de autônomo, lucros e dividendos |
| R-4020 | Pagamentos e retenções a **pessoas jurídicas** | IR, PIS, Cofins e CSLL retidos na contratação de serviços profissionais |
| R-2099 / R-4099 | Fechamento | Encerra o período |

Desde 2023, a série R-4000 substituiu a antiga **DIRF** para as retenções de Imposto de Renda e contribuições.

## Quem é obrigado

Em linhas gerais, entrega a EFD-Reinf quem, no mês:

- **contrata serviços** com cessão de mão de obra ou empreitada, com retenção de INSS;
- **presta** esses serviços e sofreu retenção;
- **retém** IR, CSLL, PIS ou Cofins de pagamentos feitos a pessoas físicas ou jurídicas;
- adquire produção rural, patrocina clube de futebol ou recolhe CPRB;
- paga **lucros e dividendos**, nas hipóteses que exigem informação.

Isso inclui empresas do **Simples Nacional** e até MEI em situações específicas. Uma empresa do Simples que paga aluguel a uma pessoa física, por exemplo, pode ter de reter e informar o IR.

## Lucros e dividendos em 2026

Com a **Lei nº 15.270/2025**, a distribuição de lucros acima de R$ 50 mil por mês a uma mesma pessoa física passou a ter retenção de 10% de IR na fonte. Essas retenções, e em alguns casos os lucros distribuídos mesmo sem retenção, precisam ser informados na EFD-Reinf. Os detalhes estão em [Dividendos em 2026: retenção de 10% na fonte](/blog/dividendos-2026-retencao-10-por-cento/).

## Prazo

A EFD-Reinf mensal deve ser transmitida **até o dia 15 do mês seguinte** ao dos fatos. Desde a alteração de 2023, se o dia 15 não for dia útil, o prazo passa para o **primeiro dia útil seguinte**.

> **Exemplo com as datas de agora:** competência outubro de 2026.
> O dia 15/11/2026 é domingo (e feriado da Proclamação da República).
> Prazo de entrega: **segunda, 16/11/2026**.

Depois de fechar a Reinf (e o eSocial), a DCTFWeb é transmitida e o DARF gerado. O DARF de outubro vence em **19/11/2026**, por causa do feriado do dia 20.

## Exemplo de retenção

> Uma empresa do Lucro Presumido contrata serviço de limpeza com cessão de mão de obra, nota fiscal de R$ 10.000.
> Retenção de INSS: 11% × R$ 10.000 = **R$ 1.100,00**.
> A empresa paga R$ 8.900 ao prestador, informa a retenção no evento R-2010 e recolhe os R$ 1.100 pela DCTFWeb.
> A empresa de limpeza informa o mesmo valor no R-2020 e compensa a retenção no INSS da própria folha.

Se as duas empresas informarem valores diferentes, surge divergência nos sistemas da Receita.

## E se não houver movimento?

Quando a empresa não tem nenhum fato a informar na Reinf, em regra não há envio mensal. Mas é preciso cuidado: basta uma retenção ou um pagamento a pessoa física para o mês passar a exigir a escrituração. Confira com o contador antes de assumir que "não tem Reinf".

## O que acontece se atrasar

- **Multa por atraso** na entrega, calculada sobre os tributos informados ou com valor mínimo por mês;
- **DCTFWeb incompleta**, gerando débitos sem a retenção correspondente;
- **pendência para a Certidão Negativa de Débitos**;
- divergência entre o que foi retido por você e o que o prestador compensou.

## O que fazer agora

Separe as notas de serviços tomados e os pagamentos a pessoas físicas de cada mês (aluguéis, autônomos, comissões) e envie ao contador até o dia 5. Se a sua empresa distribui lucros altos aos sócios, confira como a Reinf está sendo preenchida desde 2026. E anote: Reinf de outubro até **16/11**, DARF até **19/11**.
