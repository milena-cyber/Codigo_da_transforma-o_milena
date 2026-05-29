from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# =========================
# CRIA BANCO E TABELA
# =========================

conn = sqlite3.connect("usuarios.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT
)
""")

conn.commit()
conn.close()

# =========================
# ROTA POST
# =========================

@app.route("/cadastrar", methods=["POST"])
def cadastrar():

    dados = request.get_json()

    nome = dados["nome"]
    email = dados["email"]

    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO usuarios (nome, email)
    VALUES (?, ?)
    """, (nome, email))

    conn.commit()
    conn.close()

    return jsonify({
        "mensagem": "Usuário salvo no banco!"
    })


if __name__ == "__main__":
    app.run(debug=True)