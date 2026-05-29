import urllib.request
import json

cidade = "São Paulo"
api_key = "SUA_API_KEY"

url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang=pt_br&units=metric"

# Fazendo requisição
resposta = urllib.request.urlopen(url)

# Convertendo resposta para JSON
dados = json.loads(resposta.read())

print(dados)