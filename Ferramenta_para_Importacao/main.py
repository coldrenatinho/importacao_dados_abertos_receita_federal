from concurrent.futures import ThreadPoolExecutor, as_completed
from conexao_sql_server import ConexaoSQLServer
from pandas_implementacao import Pandas
from importador_sql import ImportadorSQL
from listar_arquivos import ListarArquivos

MAX_TREADS = 5
def processar_arquivo(path, tipo, engine):
    """Função que lê o arquivo e insere no SQL"""
    try:
        meu_objeto = Pandas(path, tipo.name)
        df = meu_objeto.criar_dataframe()
        importador = ImportadorSQL(engine, df)
        importador.inserir_tabela(tipo.name)
        return f"{path} importado com sucesso ({len(df)} linhas)"
    except Exception as e:
        return f"Erro ao importar {path}: {e}"

def main():
    # Conexão SQL Server
    criar_conexao = ConexaoSQLServer(
        server="localhost",
        database="Importacao_Dados_Receita_Federal",
        username="federal",
        password="SenhaForte123!"
    )
    criar_conexao.test_connection()
    engine = criar_conexao.get_enige()

    # Listar arquivos
    path_dados = r"F:\Introducao a Eng de Dados\Importacao dados aberto Receita Federal\Importacao dos dados\Dados_Brutos"
    lista_arquivos = ListarArquivos(path_dados)
    resultados = lista_arquivos.listar_arquivos()

    # Preparar todos os jobs
    jobs = []
    for arquivo in resultados:
        for path in arquivo.paths:
            jobs.append((path, arquivo.tipo, engine))

    # Executar em Threads
    max_threads= MAX_TREADS
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        future_to_path = {executor.submit(processar_arquivo, path, tipo, engine): path for path, tipo, engine in jobs}

        for future in as_completed(future_to_path):
            resultado = future.result()
            print(resultado)

if __name__ == '__main__':
    main()
