import os

PATH = r"F:\Introducao a Eng de Dados\Importacao dados aberto Receita Federal\Importacao dos dados\Dados_Brutos\Cnaes\F.K03200$Z.D50809.CNAECSV"

class VerificarPATH:
    def __init__(self, path):
        self.path = path

    def verificar_pach(self):
        if os.path.exists(PATH):
            print("Arquivo encontrado!")
        else:
            print("Arquivo NÃO encontrado!")

a = VerificarPATH(PATH)
a.verificar_pach()