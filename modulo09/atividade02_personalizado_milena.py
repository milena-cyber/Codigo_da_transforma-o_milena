# Exceção personalizada
class SaldoInsuficienteError(Exception):
    pass


class ContaBancaria:

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def sacar(self, valor):

        if valor > self.saldo:
            raise SaldoInsuficienteError(
                "Saldo insuficiente para realizar o saque."
            )

        self.saldo -= valor

        print(f"Saque realizado com sucesso.")
        print(f"Saldo restante: R${self.saldo}")


# Teste
conta = ContaBancaria("Milena", 500)

try:
    conta.sacar(700)

except SaldoInsuficienteError as erro:
    print(f"Erro: {erro}")