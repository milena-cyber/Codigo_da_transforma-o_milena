import json

# Dicionário
clientes = {

    "nome": "Milena",

    "idade": 17,

    "cidade": "São Paulo"
}

# Salvar JSON
with open("clientes.json", "w") as arquivo:

    json.dump(clientes, arquivo, indent=4)

# Ler JSON
with open("clientes.json", "r") as arquivo:

    dados = json.load(arquivo)

print(dados)