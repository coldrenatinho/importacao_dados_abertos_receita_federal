from dataclasses import  dataclass
from typing import  List, Optional

@dataclass()
class TipoArquivo:
    extensao: str
    nome: str
    campos: List[str]
    descricao: Optional[str] = None

    def imprimir_info(self):
        print(f"Extensão: {self.extensao}")
        print(f"Nome: {self.nome}")
        print(f"Campos: {', '.join(self.campos) if self.campos else 'Nenhum'}")
        if self.descricao:
            print(f"Descrição: {self.descricao}")


DICIONARIO = {
    ".CNAECSV": {"nome": "CNAES", "campos": ["CNAE_Fiscal", "Denominacao"]},
    ".EMPRECSV": {"nome": "EMPRESAS", "campos": ["CNPJ", "Razao_Social"]},
    ".ESTABELE": {"nome": "ESTABELECIMENTOS", "campos": ["CNPJ", "Nome_Estabelecimento"]},
    ".MOTICSV": {"nome": "MOTIVOS", "campos": ["Codigo_Motivo", "Descricao"]},
    ".MUNICCSV": {"nome": "MUNICIPIOS", "campos": ["Codigo_Municipio", "Nome_Municipio"]},
    ".NATJUCSV": {"nome": "NATUREZAS", "campos": ["Codigo_Natureza", "Descricao"]},
    ".PAISCSV": {"nome": "PAISES", "campos": []},
    ".QUALSCSV": {"nome": "QUALIFICACOES", "campos": []},
    ".D50809": {"nome": "SIMPLES", "campos": []},
    ".SOCIOCSV": {"nome": "SOCIOS", "campos": []},
}


