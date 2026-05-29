from django.shortcuts import render, redirect
from .models import Produto

# LISTAR
def listar_produtos(request):

    produtos = Produto.objects.all()

    return render(request, "listar.html", {
        "produtos": produtos
    })


# CADASTRAR
def cadastrar_produto(request):

    if request.method == "POST":

        Produto.objects.create(
            nome=request.POST["nome"],
            descricao=request.POST["descricao"],
            preco=request.POST["preco"],
            quantidade=request.POST["quantidade"]
        )

        return redirect("/")

    return render(request, "cadastrar.html")


# EXCLUIR
def excluir_produto(request, id):

    produto = Produto.objects.get(id=id)

    produto.delete()

    return redirect("/")