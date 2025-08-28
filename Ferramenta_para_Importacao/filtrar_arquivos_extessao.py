class ListarArquivosExtensao:
from dicionario import DICIONARIO

    def __init__(self, arquivos, DICIONARIO):
        self.arquivos = arquivos
        self.extensoes = DICIONARIO

    def filtrar_arquivos(self):
        resultados = []
        for tipo in self.extensoes:
            paths_tipo = [path for path in self.arquivos if path.upper().endswith(tipo.extensao)]
            if paths_tipo:
                resultados.append(TipoArquivoEncontrado(tipo.name, paths_tipo))
        return resultados