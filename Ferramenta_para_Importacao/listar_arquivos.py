import os

class ListarArquivosSimples:
    def __init__(self, root_path):
        self.root_path = root_path
        self.paths = self._listar_arquivos()

    def _listar_arquivos(self):
        arquivos = []
        for dirpath, _, filenames in os.walk(self.root_path):
            for filename in filenames:
                full_path = os.path.join(dirpath, filename)
                arquivos.append(full_path)
        return arquivos

    def listar_arquivos(self):
        return self.paths

    def imprimir_arquivos(self):
        for path in self.paths:
            print(path)

# Exemplo de uso
# arquivo = ListarArquivosSimples(r"F:\Introducao a Eng de Dados\Importacao dados aberto Receita Federal\Importacao dos dados\Dados_Brutos")
# arquivo.imprimir_arquivos()