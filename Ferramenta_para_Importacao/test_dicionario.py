import unittest
from Ferramenta_para_Importacao.dicionario import TipoArquivo, DICIONARIO

class TestTipoArquivo(unittest.TestCase):
    def test_exportar_como_dict(self):
        for extensao, info in DICIONARIO.items():
            tipo = TipoArquivo(
                extensao=extensao,
                nome=info["nome"],
                campos=info["colunas"]
            )
            esperado = {
                "extensao": extensao,
                "nome": info["nome"],
                "campos": info["colunas"],
                "descricao": None
            }
            self.assertEqual(tipo.exportar_como_dict(), esperado)

if __name__ == "__main__":
    unittest.main()