from dataclasses import  dataclass
from typing import  List, Optional

@dataclass()
class TipoArquivo:
    extensao: str
    nome: str
    colunas: List[str]
    descricao: Optional[str] = None


    def imprimir_info(self):
        print(f"Extensão: {self.extensao}")
        print(f"Nome: {self.nome}")
        print(f"Campos: {', '.join(self.campos) if self.campos else 'Nenhum'}")
        if self.descricao:
            print(f"Descrição: {self.descricao}")


    def exportar_como_dict(self):
        return {
            "extensao": self.extensao,
            "nome": self.nome,
            "campos": self.campos,
            "descricao": self.descricao
        }

## TODO: VERIFICAR COMO CRIAR CONTRANTO NO SQL SERVER PARA OS CAMPOS
DICIONARIO = {
    ".CNAECSV": {
        "nome": "CNAES",
        "colunas": [
            "Código",                                           #ok
            "Descrição"                                         #ok
        ]
    },
    ".EMPRECSV": {
        "nome": "EMPRESAS",
        "colunas": [
            "CNPJ Básico",                                      #ok
            "Razão Social / Nome Empresarial",                  #ok
            "Natureza Jurídica",                                #ok
            "Qualificação do Responsável",                      #ok
            "Capital Social da Empresa",                        #ok
            "Porte da Empresa",                                 #ok
            "Ente Federativo Responsável"                       #ok
        ]
    },
    ".ESTABELE": {
        "nome": "ESTABELECIMENTOS",
        "colunas": [
            "CNPJ Básico",                                      #OK
            "CNPJ Ordem",                                       #OK
            "CNPJ DV",                                          #OK
            "Identificador Matriz/Filial",                      #Verificar
            "Nome Fantasia",                                    #ok
            "Situação Cadastral",                               #ok
            "Data Situação Cadastral",                          #ok
            "Motivo Situação Cadastral",                        #ok
            "Nome da Cidade no Exterior",                       #ok
            "País",                                             #ok
            "Data de Início da Atividade",                      #ok
            "CNAE Fiscal Principal",                            #ok
            "CNAE Fiscal Secundária",                           #ok
            "Tipo de Logradouro",                               #ok
            "Logradouro",                                       #ok
            "Número",                                           #ok
            "Complemento",                                      #ok
            "Bairro",                                           #ok
            "CEP",                                              #ok
            "UF",                                               #ok
            "Município",                                        #ok
            "DDD 1",                                            #ok
            "Telefone 1",                                       #ok
            "DDD 2",                                            #ok
            "Telefone 2",                                       #ok
            "DDD do Fax",                                       #ok
            "Fax",                                              #ok
            "Correio Eletrônico",                               #ok
            "Situação Especial",                                #ok
            "Data da Situação Especial"                         #ok
        ]
    },
    ".MOTICSV": {
        "nome": "MOTIVOS",
        "colunas": [
            "Codigo",                                           #  Código do motivo
            "Descrição"                                         # Descrição do motivo
        ]
    },
    ".MUNICCSV": {
        "nome": "MUNICIPIOS",
        "colunas": [
            "Código",                                           # Código do município
            "Descrição"                                         # Nome do município
        ]
    },
    ".NATJUCSV": {
        "nome": "NATUREZAS",
        "colunas": [
            "Código",                                           # Código da natureza jurídica
            "Descrição"                                         # Nome da natureza jurídica
        ]
    },
    ".PAISCSV": {
        "nome": "PAISES",
        "colunas": [
            "Código",                                           # Código do país
            "Descrição"                                         # Nome do país
        ]
    },
    ".QUALSCSV": {
        "nome": "QUALIFICACOES",
        "colunas": [
            "Código",                                           # Código da qualificação
            "Descrição"                                         # Nome da qualificação
        ]
    },
    ".D50809": {
        "nome": "SIMPLES",
        "colunas": [
            "CNPJ Básico",                                      #ok
            "Opção pelo Simples",                               #ok
            "Data de Opção pelo Simples",                       #ok
            "Data de Exclusão do Simples",                      #ok
            "Opção pelo MEI",                                   #ok
            "Data de Opção pelo MEI",                           #ok
            "Data de Exclusão do MEI"                           #ok
        ]
    },
    ".SOCIOCSV": {
        "nome": "SOCIOS",
        "colunas": [
            "CNPJ Básico",                                      #ok
            "Identificador de Sócio",                           #ok
            "Nome do Sócio",                                    #ok
            "CNPJ/CPF do Sócio",                                #ok
            "Qualificação do Sócio",                            #ok
            "Data de Entrada na Sociedade",                     #ok
            "País",                                             #ok
            "Representante Legal",                              #ok
            "Nome do Representante",                            #ok
            "Qualificação do Representante Legal",              #ok
            "Faixa Etária"                                      #ok
        ]
    },
}





