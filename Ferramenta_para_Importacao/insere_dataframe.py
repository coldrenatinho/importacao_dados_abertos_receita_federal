## Recebe a conexão e o DataFrame e insere no SQL Server
import time

class ImportadorSQL:
    def __init__(self, engine, dataframe, table_name):
        self.engine = engine
        self.df = dataframe
        self.table_name = table_name

    def inserir_tabela(self, if_exists="append", dtype=None, chunksize=1000):
        """
        Insere o DataFrame no SQL Server.
        :param tabela: Nome da tabela de destino
        :param if_exists: "append" | "replace" | "fail"
        :param dtype: dicionário com tipos das colunas (opcional)
        :param chunksize: quantidade de linhas por batch (para performance)
        """
        if self.df is None:
            print("Nenhum DataFrame fornecido.")
            return

        try:

            for i, chunk in enumerate(range(0, len(self.df), chunksize)):
                print(time.strftime('%H:%M:%S'))
                print(f"Inserindo lote {i + 1}")
                self.df.to_sql(
                    name=self.table_name,  # Nome da tabela
                    con=self.engine,  # Conexão com o banco
                    if_exists=if_exists,  # O que fazer se a tabela já existir
                    index=False,  # Não inserir o índice do DataFrame como coluna
                    dtype=dtype,  # Tipos das colunas
                    # method="multi",
                    chunksize=chunksize  # Tamanho do lote (batch)
                )
                print(f"Dados inseridos com sucesso na tabela '{self.table_name}'.")
                print(f"Número de linhas inseridas: {len(self.df)}")
                print(f"Tamanho do DataFrame (memória): {self.df.memory_usage(deep=True).sum()} bytes")
                print("Preview das primeiras linhas:")
                print(self.df.head())
                print("-" * 40)
        except Exception as e:
            print(time.strftime('%H:%M:%S'))
            print(f"Erro ao inserir no SQL: {e}")
            print("-" * 40)
