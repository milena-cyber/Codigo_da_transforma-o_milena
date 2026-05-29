lista_compras = []

while True:

    print("\n=== LISTA DE COMPRAS ===")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Ver lista")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    # ADICIONAR
    if opcao == "1":

        item = input("Digite o item: ")

        lista_compras.append(item)

        print(f"{item} adicionado!")

    # REMOVER
    elif opcao == "2":

        item = input("Digite o item para remover: ")

        if item in lista_compras:

            lista_compras.remove(item)

            print(f"{item} removido!")

        else:

            print("Item não encontrado.")

    # VISUALIZAR
    elif opcao == "3":

        print("\nLista de compras:")

        for item in lista_compras:
            print(item)

    # SAIR
    elif opcao == "4":

        print("Encerrando programa...")
        break

    else:

        print("Opção inválida.")