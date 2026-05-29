import urllib.request
import urllib.parse
import json

api_key = "SUA_API_KEY"

filme = input("Digite o nome do filme: ")

# Corrige espaços e caracteres especiais
filme_formatado = urllib.parse.quote(filme)

url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={filme_formatado}&language=pt-BR"

try:

    resposta = urllib.request.urlopen(url)

    dados = json.loads(resposta.read())

    resultado = dados["results"][0]

    titulo = resultado["title"]
    sinopse = resultado["overview"]
    genero = resultado["genre_ids"]

    print(f"\nTítulo: {titulo}")
    print(f"Sinopse: {sinopse}")
    print(f"Gêneros IDs: {genero}")

except IndexError:
    print("Filme não encontrado.")

except Exception as erro:
    print(f"Erro: {erro}")