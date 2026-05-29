import csv

# Salvar nota
with open("notas.csv", "w", newline="") as arquivo:

    escritor = csv.writer(arquivo)

    escritor.writerow(["Nome", "Nota"])

    escritor.writerow(["Ana", 9])

    escritor.writerow(["Carlos", 8])

# Ler arquivo CSV
with open("notas.csv", "r") as arquivo:

    leitor = csv.reader(arquivo)

    for linha in leitor:

        print(linha)