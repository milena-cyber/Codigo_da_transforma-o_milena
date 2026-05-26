# Classe base
class Carro:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")


# Classe filha
class CarroEletrico(Carro):

    def __init__(self, marca, modelo, autonomia_bateria):

        super().__init__(marca, modelo)

        self.autonomia_bateria = autonomia_bateria

    def exibir_info(self):
        super().exibir_info()
        print(f"Autonomia: {self.autonomia_bateria} km")


carro2 = CarroEletrico("Tesla", "Model S", 600)

carro2.exibir_info()