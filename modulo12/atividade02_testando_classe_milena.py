import unittest


class Calculadora:

    def somar(self, a, b):
        return a + b

    def dividir(self, a, b):
        return a / b


class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()

    # Teste da soma
    def test_somar(self):
        self.assertEqual(self.calc.somar(10, 5), 15)

    # Teste da divisão
    def test_dividir(self):
        self.assertEqual(self.calc.dividir(10, 2), 5)


unittest.main()