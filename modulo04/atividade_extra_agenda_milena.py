agenda = {}

while True:

    print("\n=== AGENDA DE CONTATOS ===")
    print("1 - Adicionar contato")
    print("2 - Remover contato")
    print("3 - Buscar contato")
    print("4 - Ver contatos")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    # ADICIONAR
    if opcao == "1":

        nome = input("Nome: ")

        telefone = input("Telefone: ")

        agenda[nome] = telefone

        print("Contato adicionado!")

    # REMOVER
    elif opcao == "2":

        nome = input("Nome do contato: ")

        if nome in agenda:

            del agenda[nome]

            print("Contato removido!")

        else:

            print("Contato não encontrado.")

    # BUSCAR
    elif opcao == "3":

        nome = input("Nome do contato: ")

        if nome in agenda:

            print(f"Telefone: {agenda[nome]}")

        else:

            print("Contato não encontrado.")

    # VISUALIZAR
    elif opcao == "4":

        print("\n=== CONTATOS ===")

        for nome, telefone in agenda.items():

            print(f"{nome}: {telefone}")

    # SAIR
    elif opcao == "5":

        print("Encerrando agenda...")
        break

    else:

        print("Opção inválida.")