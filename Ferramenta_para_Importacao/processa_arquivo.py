from criar_dataframe_pandas import Pandas
from insere_dataframe import ImportadorSQL
import time

class ProcessaArquivo:
    @staticmethod
    def processar_arquivo(path, colunas_dataframe, engine, nome_tabela):
        """Função que lê o arquivo e insere no SQL
        A partir do dicionario que é listado um objeto contendo o endereço onde está o CSV, uma lista com as colunas do DataFrame
        e o nome da tabela no SQL Server
        1. Cria o DataFrame
        2. Insere o DataFrame na tabela SQL
        3. Retorna uma mensagem de sucesso ou erro
        4. Essa função é chamada por cada thread
        5. A função é chamada dentro de um bloco try/except para capturar erros
        """
        try:
            meu_objeto = Pandas(colunas_dataframe, path)                                                          #Name e path
            df = meu_objeto.criar_dataframe()                                                                     #Instancia o Data Frame
            importador = ImportadorSQL(engine=engine, dataframe=df, table_name=nome_tabela)                       #Instacia o interpletados
            importador.inserir_tabela()
            print(time.strftime('%H:%M:%S'))
            return f"Arquivo {path} importado com sucesso.\n\n\n\n\n"
        except Exception as e:
            return f"Erro ao importar {path}: {e}"