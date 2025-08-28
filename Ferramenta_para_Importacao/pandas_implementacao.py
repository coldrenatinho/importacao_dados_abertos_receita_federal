import pandas as pd
from dicionario import TipoArquivo

## Criar uma classe para importar os dados e criar uma lista para ler todos os arquivo em uma array de dados
class Pandas:
    def __init__(self, path, TipoArquivo):
        self.path = path
        self.nome = TipoArquivo.
        self.df = None                                                        # Inicializa o atributo dentro da classe

    # Cria um Data Frame do dados a partir do arquivo CSV
    def criar_dataframe(self):
        self.df = pd.read_csv(
            self.path,                                                        #Dados de entrada
            sep=';',                                                          #Separador utilizado no arquivo
            encoding='latin1',                                                #Encoder dos dados
            dtype=str                                                         #Formatar dados como String
        )
        return self.df                                                        #Retorna o DataFrame

    def head(self, n=5):
        if self.df is not None:
            return self.df.head(n)
        else:
            return "DataFrame não foi criado ainda. Use criar_dataframe() primeiro"

# meu_objeto = Pandas(PATH, "CNAE")
#
# meu_objeto.criar_dataframe()
#
# print(meu_objeto.head())


