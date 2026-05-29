from django.test import TestCase

from .models import Produto


class ProdutoTest(TestCase):

    # Teste de criação de produto
    def test_criar_produto(self):

        produto = Produto.objects.create(

            nome = "Notebook",

            descricao = "Notebook Gamer",

            preco = 5000,

            quantidade = 10
        )

        # Verificações
        self.assertEqual(produto.nome, "Notebook")

        self.assertEqual(produto.preco, 5000)

        self.assertEqual(produto.quantidade, 10)