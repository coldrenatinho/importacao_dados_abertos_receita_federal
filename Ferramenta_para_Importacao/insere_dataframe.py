## Recebe a conexão e o DataFrame e insere no SQL Server
import time

class ImportadorSQL:
    def __init__(self, engine, dataframe, table_name):
        self.engine = engine
        self.df = dataframe
        self.table_name = table_name

    def inserir_tabela(self, if_exists="append", dtype=None, chunksize=30000):
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
            for i in range(0, len(self.df), chunksize):
                chunk_df = self.df.iloc[i:i + chunksize]
                print(time.strftime('%H:%M:%S'))
                print(f"Inserindo lote {(i // chunksize) + 1}")
                chunk_df.to_sql(
                    name=self.table_name,
                    con=self.engine,
                    if_exists=if_exists if i == 0 else "append",  # só cria/recria no primeiro lote
                    index=False,
                    dtype=dtype,
                    #method="multi",  # mais eficiente
                )

                print(f"Lote {(i // chunksize) + 1} inserido com sucesso! ({len(chunk_df)} linhas)")
                print("-" * 40)

        except Exception as e:
            print(time.strftime('%H:%M:%S'))
            print(f"Erro ao inserir no SQL: {e}")
            print("-" * 40)
