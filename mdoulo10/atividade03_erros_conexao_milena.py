
import urllib.error
import json

cidade = "São Paulo"
api_key = "SUA_API_KEY"

url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang=pt_br&units=metric"

try:

    resposta = urllib.request.urlopen(url)

    dados = json.loads(resposta.read())

    temperatura = dados["main"]["temp"]
    clima = dados["weather"][0]["description"]

    print(f"Temperatura: {temperatura}°C")
    print(f"Clima: {clima}")

except urllib.error.HTTPError:
    print("Erro HTTP na requisição.")

except urllib.error.URLError:
    print("Erro de conexão com a internet.")

except Exception as erro:
    print(f"Ocorreu um erro: {erro}")