import sqlite3

conn = sqlite3.connect("clientes.db")
cursor = conn.cursor()

# Busca clientes com nome começando em A
cursor.execute("""
SELECT * FROM Clientes
WHERE nome LIKE 'A%'
""")

clientes = cursor.fetchall()

print("Clientes encontrados:\n")

for cliente in clientes:
    print(cliente)

conn.close()