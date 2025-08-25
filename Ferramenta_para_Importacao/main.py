from conexao_sql_server import ConexaoSQLServer
from pandas_implementacao import Pandas
from importador_sql import ImportadorSQL
from listar_arquivos import ListarArquivos
from enums import TipoArquivo

def main():
    # 1. Conexão com SQL Server
    criar_conexao = ConexaoSQLServer(
        server="localhost",
        database="Importacao_Dados_Receita_Federal",
        username="federal",
        password="SenhaForte123!"
    )
    criar_conexao.test_connection()
    engine = criar_conexao.get_enige()

    # 2. Listar todos os arquivos
    path_dados = r"F:\Introducao a Eng de Dados\Importacao dados aberto Receita Federal\Importacao dos dados\Dados_Brutos"
    lista_arquivos = ListarArquivos(path_dados)
    resultados = lista_arquivos.listar_arquivos()

    # 3. Iterar sobre os tipos de arquivos
    for arquivo in resultados:
        if not arquivo.paths:  # pula se não houver arquivos
            continue

        print(f"\nImportando {arquivo.tipo.name} ({len(arquivo.paths)} arquivos)...")

        for path in arquivo.paths:
            # Cria DataFrame
            meu_objeto = Pandas(path, arquivo.tipo.name)
            df = meu_objeto.criar_dataframe()

            # Insere no SQL Server
            importador = ImportadorSQL(engine, df)
            importador.inserir_tabela(arquivo.tipo.name)

            print(f"  - {path} importado ({len(df)} linhas)")

if __name__ == '__main__':
    main()


