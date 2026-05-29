import sqlite3

conn = sqlite3.connect("clientes.db")
cursor = conn.cursor()

# =========================
# INSERT
# =========================

cursor.execute("""
INSERT INTO Clientes (nome, email)
VALUES (?, ?)
""", ("Milena", "milena@gmail.com"))

conn.commit()

print("Cliente cadastrado!")

# =========================
# SELECT
# =========================

cursor.execute("SELECT * FROM Clientes")

clientes = cursor.fetchall()

print("\nLista de clientes:")

for cliente in clientes:
    print(cliente)

# =========================
# UPDATE
# =========================

cursor.execute("""
UPDATE Clientes
SET email = ?
WHERE nome = ?
""", ("novoemail@gmail.com", "Milena"))

conn.commit()

print("\nCliente atualizado!")

# =========================
# DELETE
# =========================

cursor.execute("""
DELETE FROM Clientes
WHERE nome = ?
""", ("Milena",))

conn.commit()

print("Cliente removido!")

conn.close()