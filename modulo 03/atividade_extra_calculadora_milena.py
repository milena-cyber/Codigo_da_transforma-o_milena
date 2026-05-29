while True:

    print("\n=== CALCULADORA ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    # SOMA
    if opcao == "1":

        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))

        resultado = numero1 + numero2

        print(f"Resultado: {resultado}")

    # SUBTRAÇÃO
    elif opcao == "2":

        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))

        resultado = numero1 - numero2

        print(f"Resultado: {resultado}")

    # SAIR
    elif opcao == "3":

        print("Encerrando calculadora...")
        break

    else:

        print("Opção inválida.")
        