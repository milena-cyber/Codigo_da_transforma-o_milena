class Carro:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")

    def __str__(self):
        return f"{self.marca} {self.modelo}"


carro1 = Carro("Toyota", "Corolla")

carro1.exibir_info()
print(carro1)