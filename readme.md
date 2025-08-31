# Importação de Dados Abertos da Receita Federal

Este repositório foi desenvolvido como parte da disciplina **INTRODUÇÃO À ENGENHARIA DE DADOS**. O objetivo é importar, tratar e armazenar os dados públicos do Cadastro Nacional da Pessoa Jurídica (CNPJ) disponibilizados pela Receita Federal do Brasil.

## Bibliotecas Utilizadas

- **pandas**: Manipulação e análise de dados tabulares.
- **numpy**: Suporte a operações numéricas e vetoriais.
- **SQLAlchemy**: Conexão e integração com o banco de dados SQL Server.
- **python-dateutil, pytz, tzdata**: Tratamento de datas e fusos horários.

Instalação das dependências:
```bash
pip install -r requirements.txt
```

## Como o Projeto foi Construído

1. **Coleta dos Dados**  
   Download dos arquivos públicos do CNPJ a partir dos links oficiais.

2. **Leitura e Tratamento**  
   Utilização do `pandas` para ler os arquivos, tratar colunas e preparar os dados conforme o layout oficial.

3. **Modelagem de Banco de Dados**  
   Criação das tabelas no SQL Server utilizando scripts SQL baseados no dicionário de dados da Receita Federal.

4. **Importação dos Dados**  
   Scripts Python realizam a conexão com o SQL Server (`pyodbc`) e inserem os dados tratados nas tabelas correspondentes.

5. **Validação**  
   Métodos para testar a conexão, visualizar amostras dos dados e garantir a integridade da importação.

## Referências e Fontes de Dados

- Repositório de referência: [aphonsoar/Receita\_Federal\_do\_Brasil\_-\_Dados\_Publicos\_CNPJ](https://github.com/aphonsoar/Receita_Federal_do_Brasil_-_Dados_Publicos_CNPJ?tab=readme-ov-file)
- Fonte oficial dos dados: [dados.gov.br - Cadastro Nacional da Pessoa Jurídica - CNPJ](https://dados.gov.br/dados/conjuntos-dados/cadastro-nacional-da-pessoa-juridica---cnpj)
- Layout e Dicionário de Dados: [CNPJ Metadados PDF](https://www.gov.br/receitafederal/dados/cnpj-metadados.pdf)
- Scripts SQL deste projeto: [coldrenatinho/importacao\_dados\_abertos\_receita\_federal](https://github.com/coldrenatinho/importacao_dados_abertos_receita_federal)
- Documentação do SQLAlchemy: [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/20/)
- Documentação do pandas: [pandas Documentation](https://pandas.pydata.org/docs/)
- Documentação do NumPy: [NumPy Documentation](https://numpy.org/doc/)

## Período dos Dados Utilizados

- Dados referentes a **Agosto de 2025**

## Ferramentas Utilizadas

- Banco de Dados: [SQL Server - Download](https://www.microsoft.com/pt-br/sql-server/sql-server-downloads?msockid=3e2ced33f5846be9242bf8e6f4086a19)
- Curso recomendado: [Curso de SQL Server no YouTube](https://www.youtube.com/playlist?list=PL7iAT8C5wumpQWB8AFW7CwK2nlzh8ZdP9)

---

Sinta-se à vontade para contribuir ou sugerir melhorias!
