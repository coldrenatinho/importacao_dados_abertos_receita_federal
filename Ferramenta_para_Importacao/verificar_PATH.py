import os

class VerificarPATH:
    def __init__(self, path):
        self.path = path

    def verificar_path(self):
        if os.path.exists(self.path):
            print("Arquivo encontrado!")
            return self.path
        else:
            raise FileExistsError(f"Arquivo não encotrado: {self.path}")