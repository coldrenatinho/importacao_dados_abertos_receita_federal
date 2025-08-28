## Recebe a conexão e o DataFrame e insere no SQL Server

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
                name=tabela,                                                    #Nome da tabela
                con=self.engine,                                                #Conexão com o banco
                if_exists=if_exists,                                            #O que fazer se a tabela já existir
                index=True,                                                     #Não inserir o índice do DataFrame como coluna
                dtype=dtype,                                                    #Tipos das colunas
                method="multi",
                chunksize=chunksize                                             #Tamanho do lote (batch
            )
            print(f"Dados inseridos com sucesso na tabela '{tabela}'")
        except Exception as e:
            print(f"Erro ao inserir no SQL: {e}")
