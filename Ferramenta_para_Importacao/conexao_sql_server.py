# Cria uma conexao com o banco de dados SQL Server usando SQLAlchemy
# e testa a conexao
# IMPORTANTE: O driver pode ser alterado se necessário
import traceback
import time

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
        engine = create_engine(connection_string,  fast_executemany=True, pool_size=10, max_overflow=20, pool_timeout=30, pool_recycle=1800)
        return engine

    def test_connection(self):
        try:
            engine = self.get_enige()
            with engine.connect() as connection:
                result = connection.execute(text("SELECT 1"))
                print(time.strftime('%H:%M:%S'))
                print("Resultado da consulta de teste:", result.fetchone())
                print(f"Conexão bem-sucedida!\n"
                      f"Sevidor: '{self.server}'\n"
                      f"Nome do Bando de Dados: '{self.database}'\n"
                      )
                print("-" * 40)
            return True
        except Exception as e:
            print(time.strftime('%H:%M:%S'))
            print(f"Erro ao conectar ao banco de dados: {e}\n"
                  f"Sevidor: '{self.server}'\n" 
                  f"Banco: '{self.database}'"
                  )
            print(e)
            print("-" * 40)
            traceback.print_exc()
            return False





