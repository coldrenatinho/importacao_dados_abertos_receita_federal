from conexao_sql_server import ConexaoSQLServer
from pandas_implementacao import Pandas
from importador_sql import ImportadorSQL

def main():

    criar_conexao = ConexaoSQLServer(
        server="localhost",
        database="Importacao_Dados_Receita_Federal",
        username="federal",
        password="SenhaForte123!"
    )
    criar_conexao.test_connection()

    engine = criar_conexao.get_enige()

    PATH = r"F:\Introducao a Eng de Dados\Importacao dados aberto Receita Federal\Importacao dos dados\Dados_Brutos\Cnaes\F.K03200$Z.D50809.CNAECSV"
    meu_objeto = Pandas(PATH, "CNAE")
    df = meu_objeto.criar_dataframe()

    importador = ImportadorSQL(engine, df)

    print(importador.ver_head())

    importador.inserir_tabela("CNAE")

if __name__ == '__main__':
    main()

