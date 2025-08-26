from enum import Enum

class TipoArquivo(Enum):
    CNAES = ['.CNAECSV', 'CNAES', ['CNAE_Fiscal', 'Denominacao']]
    EMPRESAS = ['.EMPRECSV', 'EMPRESAS', ['CNPJ', 'Razao_Social']]
    ESTABELECIMENTOS = ['.ESTABELE', 'ESTABELECIMENTOS', ['CNPJ', 'Nome_Estabelecimento']]
    MOTIVOS = ['.MOTICSV', 'MOTIVOS', ['Codigo_Motivo', 'Descricao']]
    MUNICIPIOS = ['.MUNICCSV', 'MUNICIPIOS', ['Codigo_Municipio', 'Nome_Municipio']]
    NATUREZAS = ['.NATJUCSV', 'NATUREZAS', ['Codigo_Natureza', 'Descricao']]
    PAISES = ['.PAISCSV', 'PAISES']
    QUALIFICACOES = ['.QUALSCSV', 'QUALIFICACOES']
    SIMPLES = ['.D50809', 'SIMPLES']
    SOCIOS = ['.SOCIOCSV', 'SOCIOS']

    # Dados que necessitam ser procesados
    # NOME [EXTENSAO, TABELA, [estrutura da tabela (colunas)]]

    # Tipagem