import sqlite3

conn = sqlite3.connect("tarefas.db")
cursor = conn.cursor()

# Criando tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS tarefas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT
)
""")

conn.commit()

while True:

    print("\n=== GERENCIADOR DE TAREFAS ===")
    print("1 - Adicionar tarefa")
    print("2 - Ver tarefas")
    print("3 - Excluir tarefa")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    # =========================
    # ADICIONAR
    # =========================

    if opcao == "1":

        descricao = input("Digite a tarefa: ")

        cursor.execute("""
        INSERT INTO tarefas (descricao)
        VALUES (?)
        """, (descricao,))

        conn.commit()

        print("Tarefa adicionada!")

    # =========================
    # VISUALIZAR
    # =========================

    elif opcao == "2":

        cursor.execute("SELECT * FROM tarefas")

        tarefas = cursor.fetchall()

        print("\n=== LISTA DE TAREFAS ===")

        for tarefa in tarefas:
            print(tarefa)

    # =========================
    # EXCLUIR
    # =========================

    elif opcao == "3":

        id_tarefa = input("Digite o ID da tarefa: ")

        cursor.execute("""
        DELETE FROM tarefas
        WHERE id = ?
        """, (id_tarefa,))

        conn.commit()

        print("Tarefa removida!")

    # =========================
    # SAIR
    # =========================

    elif opcao == "4":

        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida.")

conn.close()