from concurrent.futures import ThreadPoolExecutor, as_completed

from Ferramenta_para_Importacao.inteface_arquivos import InterfaceArquivos
from conexao_sql_server import ConexaoSQLServer
from criar_dataframe_pandas import Pandas
from insere_dataframe import ImportadorSQL
from listar_arquivos import ListarArquivosSimples
from dicionario import DICIONARIO

MAX_TREADS = 5
ROOT_PATH = (r"F:\Introducao a Eng de Dados\Importacao dados aberto Receita Federal\Importacao dos dados\Dados_Brutos")
def processar_arquivo(path, tipo, engine):
    """Função que lê o arquivo e insere no SQL"""
    try:
        meu_objeto = Pandas() #Name e path
        df = meu_objeto.criar_dataframe() #Instancia o Data Frame
        importador = ImportadorSQL(engine, df)     #Instacia o interpletados                                 # OK não mexer
        importador.inserir_tabela()                 #Insere o Data Frame na tabela SQL
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



if __name__ == '__main__':
    main()
