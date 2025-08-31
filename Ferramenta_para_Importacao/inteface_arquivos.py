# Inteface vai receber uma lista de arquivos e o dicionario
# Vai retornar os tipos encontrados na lista de arquivos
# Assim como suas extensões, nomes e colunas
class InterfaceArquivos:
    def __init__(self, lista_full_pach_arquivos, dicionario):
        self.arquivos = lista_full_pach_arquivos
        self.dicionario = dicionario

    def listar_tipos(self):
        tipos = []
        for arquivo in self.arquivos:
            for extensao, info in self.dicionario.items():
                if arquivo.upper().endswith(extensao.upper()):
                    tipos.append({
                        "extensao": extensao,
                        "nome": info["nome"],
                        "colunas": info["colunas"],
                        "full_path": arquivo
                    })
        return tipos
    def imprimir_tipos_arquivos(self):
        interface = InterfaceArquivos(self.arquivos, self.dicionario)
        tipos = interface.listar_tipos()
        for tipo in tipos:
            print(f"Extensão: {tipo['extensao']}\nNome: {tipo['nome']}\nColunas: {tipo['colunas']}\nFull Path: {tipo['full_path']}\n{'-'*40}")


