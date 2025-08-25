# Cria uma conexao com o banco de dados SQL Server usando SQLAlchemy
# e testa a conexao
import traceback

from sqlalchemy import create_engine, text

class ConexaoSQLServer:
    def __init__(self, server, database, username, password, driver="ODBC Driver 17 for SQL Server"):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.driver = driver


    def get_connection_string(self):
        return f"mssql+pyodbc://{self.username}:{self.password}@{self.server}/{self.database}?driver={self.driver.replace(' ', '+')}"

    def get_enige(self):
        connection_string = self.get_connection_string()
        engine = create_engine(connection_string)
        return engine

    def test_connection(self):
        try:
            engine = self.get_enige()
            with engine.connect() as connection:
                result = connection.execute(text("SELECT 1"))
                print("Resultado da consulta de teste:", result.fetchone())
                print('Conexão bem-sucedida!')
            return True
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            print(e)
            traceback.print_exc()
            return False

# conexao = ConexaoSQLServer(
#     server="localhost",
#     database="Importacao_Dados_Receita_Federal",
#     username="federal",
#     password="SenhaForte123!"
# )
#
# conexao.test_connection()






