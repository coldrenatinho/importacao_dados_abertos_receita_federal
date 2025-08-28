# Novo Layout para os Dados Abertos do CNPJ

## Empresas

- **CNPJ Básico**: Número base de inscrição no CNPJ (8 primeiros dígitos).
- **Razão Social / Nome Empresarial**: Nome empresarial da pessoa jurídica.
- **Natureza Jurídica**: Código da natureza jurídica.
- **Qualificação do Responsável**: Qualificação da pessoa física responsável.
- **Capital Social da Empresa**: Valor do capital social.
- **Porte da Empresa**:
  - 00: Não informado
  - 01: Micro Empresa
  - 03: Empresa de Pequeno Porte
  - 05: Demais
- **Ente Federativo Responsável**: Preenchido para órgãos do grupo 1XXX.

---

## Estabelecimentos

- **CNPJ Básico**: Número base do CNPJ.
- **CNPJ Ordem**: Dígitos 9 a 12 do CNPJ.
- **CNPJ DV**: Dígitos 13 e 14 do CNPJ.
- **Identificador Matriz/Filial**:
  - 1: Matriz
  - 2: Filial
- **Nome Fantasia**: Nome fantasia do estabelecimento.
- **Situação Cadastral**:
  - 01: Nula
  - 02: Ativa
  - 03: Suspensa
  - 04: Inapta
  - 08: Baixada
- **Data Situação Cadastral**: Data do evento.
- **Motivo Situação Cadastral**: Código do motivo.
- **Nome da Cidade no Exterior**: Nome da cidade (se aplicável).
- **País**: Código do país.
- **Data de Início da Atividade**: Data de início.
- **CNAE Fiscal Principal**: Código da atividade principal.
- **CNAE Fiscal Secundária**: Códigos das atividades secundárias.
- **Tipo de Logradouro**: Descrição do tipo.
- **Logradouro**: Nome da rua/avenida.
- **Número**: Número do endereço.
- **Complemento**: Complemento do endereço.
- **Bairro**: Bairro do estabelecimento.
- **CEP**: Código postal.
- **UF**: Unidade da federação.
- **Município**: Código do município.
- **DDD 1 / Telefone 1**: DDD e número.
- **DDD 2 / Telefone 2**: DDD e número.
- **DDD do Fax / Fax**: DDD e número.
- **Correio Eletrônico**: E-mail.
- **Situação Especial**: Situação especial da empresa.
- **Data da Situação Especial**: Data de entrada na situação.

---

## Dados do Simples

- **CNPJ Básico**: Número base do CNPJ.
- **Opção pelo Simples**:
  - S: Sim
  - N: Não
  - (em branco): Outros
- **Data de Opção pelo Simples**: Data da adesão.
- **Data de Exclusão do Simples**: Data da exclusão.
- **Opção pelo MEI**:
  - S: Sim
  - N: Não
  - (em branco): Outros
- **Data de Opção pelo MEI**: Data da adesão.
- **Data de Exclusão do MEI**: Data da exclusão.

---

## Sócios

- **CNPJ Básico**: Número base do CNPJ.
- **Identificador de Sócio**:
  - 1: Pessoa Jurídica
  - 2: Pessoa Física
  - 3: Estrangeiro
- **Nome do Sócio**: Nome ou razão social.
- **CNPJ/CPF do Sócio**: CPF ou CNPJ (exceto estrangeiro).
- **Qualificação do Sócio**: Código da qualificação.
- **Data de Entrada na Sociedade**: Data de ingresso.
- **País**: Código do país (sócio estrangeiro).
- **Representante Legal**: CPF do representante.
- **Nome do Representante**: Nome do representante.
- **Qualificação do Representante Legal**: Código da qualificação.
- **Faixa Etária**:
  - 1: 0–12
  - 2: 13–20
  - 3: 21–30
  - 4: 31–40
  - 5: 41–50
  - 6: 51–60
  - 7: 61–70
  - 8: 71–80
  - 9: +80
  - 0: Não se aplica

---

## Tabelas de Domínio

### Países

- **Código**: Código do país.
- **Descrição**: Nome do país.

### Municípios

- **Código**: Código do município.
- **Descrição**: Nome do município.

### Qualificações de Sócios

- **Código**: Código da qualificação.
- **Descrição**: Nome da qualificação.

### Naturezas Jurídicas

- **Código**: Código da natureza jurídica.
- **Descrição**: Nome da natureza jurídica.

### CNAEs

- **Código**: Código da atividade econômica.
- **Descrição**: Nome da atividade.

