from dataclasses import  dataclass
from typing import  List, Optional

TIPOS_ARQUIVO = [
    TipoArquivo(".CNAECSV", "CNAES", ["CNAE_Fiscal", "Denominacao"]),
    TipoArquivo(".EMPRECSV", "EMPRESAS", ["CNPJ", "Razao_Social"]),
    TipoArquivo(".ESTABELE", "ESTABELECIMENTOS", ["CNPJ", "Nome_Estabelecimento"]),
    TipoArquivo(".MOTICSV", "MOTIVOS", ["Codigo_Motivo", "Descricao"]),
    TipoArquivo(".MUNICCSV", "MUNICIPIOS", ["Codigo_Municipio", "Nome_Municipio"]),
    TipoArquivo(".NATJUCSV", "NATUREZAS", ["Codigo_Natureza", "Descricao"]),
    TipoArquivo(".PAISCSV", "PAISES"),
    TipoArquivo(".QUALSCSV", "QUALIFICACOES"),
    TipoArquivo(".D50809", "SIMPLES"),
    TipoArquivo(".SOCIOCSV", "SOCIOS"),
]