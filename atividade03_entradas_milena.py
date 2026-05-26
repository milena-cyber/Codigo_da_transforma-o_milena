while True:

    try:
        idade = int(input("Digite sua idade: "))

        if idade < 0:
            print("A idade deve ser positiva.")

        else:
            print(f"Idade válida: {idade}")
            break

    except ValueError:
        print("Erro: digite apenas números inteiros.")
