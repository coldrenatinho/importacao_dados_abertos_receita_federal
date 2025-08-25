import os
from enum import Enum, auto

class TipoArquivo(Enum):
    CNAES = ".CNAECSV"
    EMPRESAS = ".EMPRECSV"
    ESTABELECIMENTOS = ".ESTABELE"
    MOTIVOS = ".MOTICSV"
    MUNICIPIOS = ".MUNICCSV"
    PAISES = ".PAISCSV"
    QUALIFICACOES = ".QUALSCSV"
    SIMPLES = ".D50809"
    SOCIOS = ".SOCIOCSV"

class ListarArquivos:
    def __init__(self, root_path):
        self.root_path = root_path
        # Dicionário para armazenar os arquivos encontrados por tipo
        self.arquivos = {tipo.name: [] for tipo in TipoArquivo}
        self._listar_arquivos()

    def _listar_arquivos(self):
        """Percorre todos os diretórios e subdiretórios, preenchendo os arquivos"""
        for dirpath, dirnames, filenames in os.walk(self.root_path):
            for filename in filenames:
                full_path = os.path.join(dirpath, filename)
                for tipo in TipoArquivo:
                    if filename.endswith(tipo.value):
                        self.arquivos[tipo.name].append(full_path)

    def listar_arquivos(self):
        """Retorna o dicionário de arquivos encontrados"""
        return self.arquivos

arquivo = ListarArquivos(r"F:\Introducao a Eng de Dados\Importacao dados aberto Receita Federal\Importacao dos dados\Dados_Brutos")
arquivos_encontrados = arquivo.listar_arquivos()
for tipo, paths in arquivos_encontrados.items():
    print(f"{tipo}:")
    for path in paths:
        print(f"  - {path}")
    if not paths:
        print("  - Nenhum arquivo encontrado")