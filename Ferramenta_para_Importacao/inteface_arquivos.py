from dicionario import DICIONARIO

# Inteface vai receber uma lista de arquivos e o dicionario
# Vai retornar os tipos encontrados na lista de arquivos
class InterfaceArquivos:
    def __init__(self, arquivos, dicionario):
        self.arquivos = arquivos
        self.dicionario = dicionario

    def listar_tipos(self):
        tipos = []
        for arquivo in self.arquivos:
            for extensao, info in self.dicionario.items():
                if arquivo.upper().endswith(extensao.upper()):
                    tipos.append({
                        "extensao": extensao,
                        "nome": info["nome"],
                        "campos": info["campos"]
                    })
        return tipos

# Exemplo de uso:
arquivos = ["empresa.EMPRECSV", "motivo.MOTICSV"]
interface = InterfaceArquivos(arquivos, DICIONARIO)
tipos_encontrados = interface.listar_tipos()

for tipo in tipos_encontrados:
    print(f"Extensão: {tipo['extensao']}")
    print(f"Nome: {tipo['nome']}")
    print(f"Campos: {tipo['campos']}")
    print("---")
