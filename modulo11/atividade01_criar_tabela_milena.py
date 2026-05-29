import sqlite3

# Criando conexão com o banco
conn = sqlite3.connect("clientes.db")

# Criando cursor
cursor = conn.cursor()

# Criando tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS Clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT
)
""")

print("Tabela criada com sucesso!")

# Salvando alterações
conn.commit()

# Fechando conexão
conn.close()