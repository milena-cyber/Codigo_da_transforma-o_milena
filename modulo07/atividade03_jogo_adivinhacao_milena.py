import random
import math

numero_secreto = random.randint(1, 100)

tentativas = 0

while True:

    palpite = int(input("Digite um número de 1 a 100: "))

    tentativas += 1

    if palpite == numero_secreto:

        print("Parabéns! Você acertou.")

        print(f"Tentativas: {tentativas}")

        break

    elif palpite < numero_secreto:

        diferenca = math.fabs(numero_secreto - palpite)

        print(f"Muito baixo! Diferença: {diferenca}")

    else:

        diferenca = math.fabs(numero_secreto - palpite)

        print(f"Muito alto! Diferença: {diferenca}")