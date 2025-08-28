import pandas as pd

class Pandas:
    def __init__(self, names, file_path):                                       # Construtor da classe
        self.colunas = names                                                    # Colunas do Data Frame
        self.path = file_path                                                   # Caminho do arquivo CSV
        self.df = None                                                          # Data Frame vazio

    # Cria um Data Frame do dados a partir do arquivo CSV
    def criar_dataframe(self):
        try:
            self.df = pd.read_csv(
                self.path,                                                        #Nome da tabela
                names=self.colunas,                                               #Colunas do Data Frame
                sep=';',                                                          #Separador utilizado no arquivo
                encoding='latin1',                                                #Encoder dos dados
                dtype=str                                                         #Formatar dados como String
           )
            return self.df.dropna().drop_duplicates().fillna('N/A')
        except Exception as e:
                print(f"Erro ao ler o arquivo: {e}")



