import os
from dataclasses import dataclass, field
from enum_arquivos import TipoArquivo

@dataclass
class ArquivoEncontrado:
    tipo: TipoArquivo
    paths: list = field(default_factory=list)

class ListarArquivos:
    def __init__(self, root_path):
        self.root_path = root_path
        # Cria uma lista de objetos ArquivoEncontrado, um para cada TipoArquivo
        self.resultados = [ArquivoEncontrado(tipo) for tipo in TipoArquivo]
        self._listar_arquivos()

    def _listar_arquivos(self):
        """Percorre todos os diretórios e subdiretórios, preenchendo os arquivos"""
        for dirpath, dirnames, filenames in os.walk(self.root_path):
            for filename in filenames:
                full_path = os.path.join(dirpath, filename)
                for arquivo in self.resultados:
                    if filename.endswith(arquivo.tipo.value):
                        arquivo.paths.append(full_path)

    def listar_arquivos(self):
        """Retorna a lista de objetos ArquivoEncontrado"""
        return self.resultados

    def imprimir_arquivos(self):
        """Imprime os arquivos encontrados por tipo"""
        for arquivo in self.resultados:
            print(f"{arquivo.tipo.name}:")
            if arquivo.paths:
                for path in arquivo.paths:
                    print(f"  - {path}")
            else:
                print("  - Nenhum arquivo encontrado")


arquivo = ListarArquivos(r"F:\Introducao a Eng de Dados\Importacao dados aberto Receita Federal\Importacao dos dados\Dados_Brutos")
arquivos_encontrados = arquivo.listar_arquivos()
arquivo.imprimir_arquivos()