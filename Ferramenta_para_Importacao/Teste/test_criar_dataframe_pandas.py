import unittest
import pandas as pd

class TestCriarDataFrame(unittest.TestCase):
    def test_criacao_dataframe(self):
        dados = {
            'nome': ['Ana', 'Bruno', 'Carlos'],
            'idade': [23, 34, 45]
        }
        df = pd.DataFrame(dados)
        self.assertEqual(list(df.columns), ['nome', 'idade'])
        self.assertEqual(df.shape, (3, 2))
        self.assertEqual(df.iloc[0]['nome'], 'Ana')
        self.assertEqual(df.iloc[1]['idade'], 34)

if __name__ == '__main__':
    unittest.main()