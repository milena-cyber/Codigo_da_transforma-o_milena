import unittest


class Calculadora:

    def dividir(self, a, b):

        if b == 0:
            raise ZeroDivisionError(
                "Não é possível dividir por zero."
            )

        return a / b


class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()

    # Testando divisão por zero
    def test_divisao_por_zero(self):

        with self.assertRaises(ZeroDivisionError):
            self.calc.dividir(10, 0)


unittest.main()