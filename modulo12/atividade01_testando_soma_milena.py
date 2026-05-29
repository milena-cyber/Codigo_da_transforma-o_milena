import unittest

# Função
def soma(a, b):
    return a + b


# Classe de teste
class TestSoma(unittest.TestCase):

    def test_soma(self):
        resultado = soma(5, 3)
        self.assertEqual(resultado, 8)


# Executa os testes
unittest.main()