import unittest

# Importa a aplicação
from app import app


class TestAPI(unittest.TestCase):

    # Configuração inicial
    def setUp(self):

        self.cliente = app.test_client()

    # Teste da rota principal
    def test_home(self):

        resposta = self.cliente.get("/")

        # Verifica status da resposta
        self.assertEqual(
            resposta.status_code,
            200
        )

        # Converte resposta para JSON
        dados = resposta.get_json()

        # Verifica mensagem
        self.assertEqual(
            dados["mensagem"],
            "API funcionando!"
        )


# Executa os testes
unittest.main()