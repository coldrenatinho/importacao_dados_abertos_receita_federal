from concurrent.futures import ThreadPoolExecutor, as_completed
import time
from inteface_arquivos import InterfaceArquivos
from conexao_sql_server import ConexaoSQLServer
from listar_arquivos import ListarArquivosSimples
from dicionario import DICIONARIO
from processa_arquivo import ProcessaArquivo


######## PARÂMETROS ########
MAX_TREADS = 2
# ROOT_PATH = (r"F:\Introducao a Eng de Dados\Importacao dados aberto Receita Federal\Importacao dos dados\Dados_Brutos")
# ROOT_PATH = (r"F:\Introducao a Eng de Dados\Importacao dados aberto Receita Federal\Importacao dos dados\Dados_Brutos\Estabelecimentos\Estabelecimentos0")
ROOT_PATH = (r"F:\Introducao a Eng de Dados\Importacao dados aberto Receita Federal\Importacao dos dados\Dados_Brutos\Estabelecimentos\TESTE")
VERSAO = "4.0"
AUTOR = "Renato A. Silva"
GIT_HUB = (r"https://github.com/coldrenhatinho")
LINKEDIN = (r"https://www.linkedin.com/in/renatoaraujo045/")
###########################
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
    lista_arquivos = arquivos.listar_arquivos()                                             # Lista de arquivos encontrados no diretório
    tipos_encontrados = InterfaceArquivos(lista_arquivos, DICIONARIO)                       # Instancia a interface de arquivos
    tipos_encontrados.imprimir_tipos_arquivos()

    tipos = tipos_encontrados.listar_tipos()  # Lista de tipos encontrados
    for tipo in tipos:
        extensao = tipo['extensao']
        nome_tabela = tipo['nome']
        colunas_dataframe = tipo['colunas']
        arquivos_filtrados = [arquivo for arquivo in lista_arquivos if arquivo.upper().endswith(extensao.upper())]
        print(f'\033[92mProcessando {len(arquivos_filtrados)} arquivo(s) com extensão {extensao} para a tabela {nome_tabela}\033[0m\n')

        start_time = time.time()
        print(time.strftime('%H:%M:%S'))
        print(f'\033[92mIniciando o processamento\033[0m')
        ############### Processamento com ThreadPoolExecutor ################
        with ThreadPoolExecutor(max_workers=MAX_TREADS) as executor:
            futures = [
                executor.submit(ProcessaArquivo.processar_arquivo, path, colunas_dataframe, engine, nome_tabela)
                for path in arquivos_filtrados
            ]
            for future in as_completed(futures):
                print(future.result())
        elapsed_time = time.time() - start_time
        print(f'\033[92mTempo total para processar arquivos com extensão {extensao}: {elapsed_time:.2f} segundos\033[0m\n')
        print("-" * 40)

if __name__ == '__main__':
    main()