import unittest
from src.classificador import classificar_numero

class TestClassificarNumero(unittest.TestCase):
    def test_numero_positivo(self):
        self.assertEqual(classificar_numero(10), "Positivo")

    def test_numero_negativo(self):
        self.assertEqual(classificar_numero(-1), "Negativo")

    def test_numero_zero(self):
        self.assertEqual(classificar_numero(0), "Zero")

if __name__ == "__main__":
    unittest.main()
