

def somar(a, b):

    return a + b


def multiplicar(a, b):

    return a * b




def saudacao(nome):

    return f"Olá, {nome}!"



while True:

    print("\n=== MENU ===")
    print("1 - Somar")
    print("2 - Multiplicar")
    print("3 - Saudação")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        print("Resultado:", somar(num1, num2))

    elif opcao == "2":

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        print("Resultado:", multiplicar(num1, num2))

    elif opcao == "3":

        nome = input("Digite seu nome: ")

        print(saudacao(nome))

    elif opcao == "4":

        print("Programa encerrado.")
        break

    else:

        print("Opção inválida.")