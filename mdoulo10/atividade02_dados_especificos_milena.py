import urllib.request
import json

cidade = "São Paulo"
api_key = "SUA_API_KEY"

url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang=pt_br&units=metric"

resposta = urllib.request.urlopen(url)

dados = json.loads(resposta.read())

temperatura = dados["main"]["temp"]
clima = dados["weather"][0]["description"]

print(f"Cidade: {cidade}")
print(f"Temperatura: {temperatura}°C")
print(f"Clima: {clima}")