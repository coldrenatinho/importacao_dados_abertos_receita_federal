import pandas as pd

class ImportadorSQL:
    def __init__(self, engine, dataframe):
        self.engine = engine
        self.df = dataframe

    def inserir_tabela(self, tabela, if_exists="append", dtype=None, chunksize=1000):
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
            self.df.to_sql(
                name=tabela,
                con=self.engine,
                if_exists=if_exists,
                index=False,
                dtype=dtype,
                method="multi",
                chunksize=chunksize
            )
            print(f"Dados inseridos com sucesso na tabela '{tabela}'")
        except Exception as e:
            print(f"Erro ao inserir no SQL: {e}")

    def ver_head(self, n=5):
        if self.df is not None:
            return self.df.head(n)
        else:
            return "DataFrame não definido."
