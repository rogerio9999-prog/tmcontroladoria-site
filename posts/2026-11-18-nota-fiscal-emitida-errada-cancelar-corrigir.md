---
titulo: "Emiti a nota fiscal errada: posso cancelar, corrigir ou preciso emitir outra?"
resumo: Valor errado, cliente trocado, CNPJ com erro. Veja o que a carta de correção resolve, quando cancelar, quando emitir nota de devolução e como o erro mexe no DAS.
data: 2026-11-18
categoria: Gestão e Controladoria
tags: [nota fiscal, NF-e, NFS-e, carta de correção, cancelamento de nota, DAS]
fontes:
  - Portal Nacional da NF-e (Receita Federal e Secretarias de Fazenda) | https://www.nfe.fazenda.gov.br/
  - Portal do Simples Nacional, PGDAS-D | https://www8.receita.fazenda.gov.br/simplesnacional/
  - Secretaria de Estado de Fazenda de Minas Gerais (SEF-MG) | https://www.fazenda.mg.gov.br/
checagem:
  - Confirmar o prazo geral de cancelamento da NF-e na legislação vigente (ajuste SINIEF) e se a SEF-MG adota prazo diferente; o texto diz apenas que o prazo é curto e fixado pelo fisco
  - Confirmar quais campos a carta de correção eletrônica não pode alterar (o texto cita valores, impostos, quantidade e dados que mudem o destinatário)
  - Confirmar como o município de Uberaba trata o cancelamento de NFS-e fora do prazo (texto geral, sem prazo)
  - Os valores do exemplo (alíquota efetiva de 6%) são ilustrativos
---

Você fechou a venda, emitiu a nota e, dois minutos depois, o cliente avisa: o CNPJ está errado. Ou o valor saiu R$ 2.000 a mais. A nota já está autorizada, o PDF já foi enviado. E agora? A resposta depende de **que erro foi, de que tipo de nota é e de quanto tempo passou**.

## Primeiro, identifique o tipo de erro

Antes de escolher o caminho, responda três perguntas:

1. **A mercadoria já saiu ou o serviço já foi prestado?** Se a operação não aconteceu (ou foi desfeita antes de acontecer), o caminho tende a ser o cancelamento.
2. **O erro altera valor, imposto ou quantidade?** Nesse caso a carta de correção não resolve.
3. **Quanto tempo passou desde a autorização?** O cancelamento tem prazo curto, definido pelo fisco.

## Carta de correção: só para erros que não mexem em valores

A carta de correção eletrônica (CC-e) existe para a NF-e, a nota de produtos. Ela serve para corrigir informações que **não alteram o valor do imposto**, como um dado de transporte, uma observação, um endereço de entrega que não mude o destinatário.

Ela **não corrige**, em regra:

- valores, quantidades e impostos;
- dados que mudem quem é o remetente ou o destinatário;
- data de emissão ou de saída.

Se o erro é de CNPJ do cliente, por exemplo, a carta de correção não serve. O mesmo vale para preço errado.

## Cancelamento: janela curta

Enquanto a mercadoria não circulou e o prazo não acabou, o caminho é **cancelar a nota** no próprio sistema emissor e emitir outra correta. O prazo para cancelar a NF-e é curto e definido pela legislação das Secretarias de Fazenda (confirme o prazo vigente no seu estado, no caso de Minas Gerais, na SEF-MG). Passou da janela, o cancelamento simples deixa de estar disponível.

Para a nota de serviço (NFS-e), as regras de cancelamento dependem do município e do emissor usado. Em muitos casos o cancelamento é feito direto no emissor dentro de um prazo; depois dele, é preciso um pedido formal à prefeitura. Veja o contexto do emissor nacional em [NFS-e padrão nacional: o que muda para a empresa](/blog/nfs-e-padrao-nacional-empresas/).

## Mercadoria já saiu e a nota está errada: devolução ou nota complementar

Quando a mercadoria circulou e o cancelamento não é mais possível, as saídas costumam ser:

- **Devolução**: o cliente devolve a mercadoria e a operação é desfeita com a documentação própria (nota de entrada ou de devolução, conforme o caso).
- **Nota complementar**: quando o valor emitido ficou menor que o correto, emite-se uma nota complementar só da diferença.

Aqui a escolha depende do imposto envolvido (ICMS, por exemplo) e das regras do estado. Nesse ponto, **fale com o seu contador antes de emitir qualquer documento novo**: uma nota emitida às pressas para consertar outra pode criar um segundo problema.

## O erro mexe no DAS?

Mexe, quando altera a receita. No Simples Nacional, o DAS é calculado sobre a receita bruta do mês, e as notas emitidas alimentam essa apuração.

Exemplo com números ilustrativos: a empresa emitiu uma nota de R$ 10.000, mas o valor correto era R$ 8.000. Foram R$ 2.000 a mais de receita. Com alíquota efetiva de 6%, o DAS sobe R$ 120 (R$ 2.000 x 0,06). Se a nota for cancelada e substituída no mesmo mês, a receita informada fica certa. Se o erro só aparece depois que o PGDAS-D foi transmitido, é preciso retificar a declaração. O passo a passo está em [Errei no PGDAS-D: como retificar](/blog/retificar-pgdas-d-corrigir-das/).

## Como reduzir erros de emissão

- **Cadastro de clientes revisado.** Confirme CNPJ ou CPF, razão social e endereço antes de emitir, de preferência consultando o cartão CNPJ.
- **Cadastro de produtos conferido.** Código fiscal (CFOP, CSOSN e, a partir da Reforma Tributária, os códigos de IBS e CBS) errado no produto se repete em toda nota. Veja [CSOSN na nota fiscal do Simples](/blog/csosn-nota-fiscal-simples/).
- **Conferência antes de transmitir.** Uma segunda pessoa, ou ao menos uma pausa de um minuto, evita a maioria dos erros de digitação.
- **Registro do erro.** Anote o motivo de cada cancelamento. Cancelamentos frequentes chamam atenção do fisco e indicam problema de processo.

## O que fazer agora

1. Se a nota é de hoje e a mercadoria não saiu, **cancele e reemita**.
2. Se a nota é antiga ou a operação aconteceu, **não improvise**: separe a nota errada, o pedido do cliente e o comprovante de pagamento e leve ao contador.
3. Confira se o erro mudou a receita do mês e, se o DAS já foi transmitido, peça a retificação.
4. Em Uberaba ou em qualquer outro município, confirme na prefeitura as regras de cancelamento da NFS-e que você usa.
