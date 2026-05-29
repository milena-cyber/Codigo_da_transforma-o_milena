from django.core.paginator import Paginator
from .models import Produto

def listar_produtos(request):

    busca = request.GET.get("busca")

    produtos = Produto.objects.all()

    # Busca por nome
    if busca:
        produtos = produtos.filter(nome__icontains=busca)

    # Paginação
    paginator = Paginator(produtos, 5)

    pagina = request.GET.get("page")

    produtos = paginator.get_page(pagina)

    return render(request, "listar.html", {
        "produtos": produtos
    })