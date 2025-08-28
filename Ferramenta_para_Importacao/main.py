from concurrent.futures import ThreadPoolExecutor, as_completed
import time

from pandas.core.indexes.base import ensure_index

from Ferramenta_para_Importacao.inteface_arquivos import InterfaceArquivos
from conexao_sql_server import ConexaoSQLServer
from criar_dataframe_pandas import Pandas
from insere_dataframe import ImportadorSQL
from listar_arquivos import ListarArquivosSimples
from dicionario import DICIONARIO

MAX_TREADS = 12
ROOT_PATH = (r"F:\Introducao a Eng de Dados\Importacao dados aberto Receita Federal\Importacao dos dados\Dados_Brutos")
def processar_arquivo(path, colunas_dataframe, engine, nome_tabela):
    """Função que lê o arquivo e insere no SQL"""
    try:
        meu_objeto = Pandas(colunas_dataframe, path)                                                          #Name e path
        df = meu_objeto.criar_dataframe()                                                                     #Instancia o Data Frame
        importador = ImportadorSQL(engine=engine, dataframe=df, table_name=nome_tabela)                                                                #Instacia o interpletados
        importador.inserir_tabela()                                                                           #Insere o Data Frame na tabela SQL
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

    arquivos = ListarArquivosSimples(ROOT_PATH)
    lista_arquivos = arquivos.listar_arquivos() # Lista de arquivos encontrados no diretório
    tipos_encontrados = InterfaceArquivos(lista_arquivos, DICIONARIO) # Instancia a interface de arquivos
    tipos_encontrados.imprimir_tipos_arquivos()

    tipos = tipos_encontrados.listar_tipos() # Lista de tipos encontrados
    for tipo in tipos:
        extensao = tipo['extensao']
        nome_tabela = tipo['nome']
        colunas_dataframe = tipo['colunas']
        # arquivos_filtrados = [arquivo for arquivo in lista_arquivos if arquivo.upper().endswith(extensao.upper())]
        arquivo = tipo['full_path']
        arquivos_filtrados = [arquivo]  # Lista de arquivos filtrados por extensão

        print(f"Processando {len(arquivos_filtrados)} arquivos com extensão {extensao} para a tabela {nome_tabela}")

        start_time = time.time()
        tipos = tipos_encontrados.listar_tipos() # Lista de tipos encontrados
        with ThreadPoolExecutor(max_workers=MAX_TREADS) as executor:
            # futures = {executor.submit(processar_arquivo, path, colunas_dataframe, engine, nome_tabela): path for path in arquivos_filtrados}
            futures = {executor.submit(processar_arquivo, path, colunas_dataframe, engine, nome_tabela): path for path
                       in arquivos_filtrados}

            for future in as_completed(futures):
                result = future.result()
                print(result)
        elapsed_time = time.time() - start_time
        print(f"Tempo total para processar arquivos com extensão {extensao}: {elapsed_time:.2f} segundos")

if __name__ == '__main__':
    main()
