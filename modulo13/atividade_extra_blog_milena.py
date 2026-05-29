from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# =========================
# BANCO DE DADOS
# =========================

conn = sqlite3.connect("blog.db")
cursor = conn.cursor()

# Tabela de usuários
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT,
    senha TEXT
)
""")

# Tabela de posts
cursor.execute("""
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT,
    conteudo TEXT
)
""")

conn.commit()
conn.close()

# =========================
# CADASTRO DE USUÁRIO
# =========================

@app.route("/registrar", methods=["POST"])
def registrar():

    dados = request.get_json()

    usuario = dados["usuario"]
    senha = dados["senha"]

    conn = sqlite3.connect("blog.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO usuarios (usuario, senha)
    VALUES (?, ?)
    """, (usuario, senha))

    conn.commit()
    conn.close()

    return jsonify({
        "mensagem": "Usuário registrado!"
    })

# =========================
# LOGIN
# =========================

@app.route("/login", methods=["POST"])
def login():

    dados = request.get_json()

    usuario = dados["usuario"]
    senha = dados["senha"]

    conn = sqlite3.connect("blog.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM usuarios
    WHERE usuario = ? AND senha = ?
    """, (usuario, senha))

    usuario_encontrado = cursor.fetchone()

    conn.close()

    if usuario_encontrado:

        return jsonify({
            "mensagem": "Login realizado!"
        })

    else:

        return jsonify({
            "mensagem": "Usuário ou senha inválidos."
        })

# =========================
# CRIAR POST
# =========================

@app.route("/posts", methods=["POST"])
def criar_post():

    dados = request.get_json()

    titulo = dados["titulo"]
    conteudo = dados["conteudo"]

    conn = sqlite3.connect("blog.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO posts (titulo, conteudo)
    VALUES (?, ?)
    """, (titulo, conteudo))

    conn.commit()
    conn.close()

    return jsonify({
        "mensagem": "Post criado!"
    })

# =========================
# LISTAR POSTS
# =========================

@app.route("/posts", methods=["GET"])
def listar_posts():

    conn = sqlite3.connect("blog.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM posts")

    posts = cursor.fetchall()

    conn.close()

    lista_posts = []

    for post in posts:

        lista_posts.append({
            "id": post[0],
            "titulo": post[1],
            "conteudo": post[2]
        })

    return jsonify(lista_posts)


# =========================
# EXECUTAR SERVIDOR
# =========================

if __name__ == "__main__":
    app.run(debug=True)