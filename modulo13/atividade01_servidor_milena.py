from flask import Flask

# Cria o servidor Flask
app = Flask(__name__)

# Rota GET
@app.route("/saudacao")
def saudacao():

    return "Olá! Servidor Flask funcionando."


# Executa o servidor
if __name__ == "__main__":
    app.run(debug=True)