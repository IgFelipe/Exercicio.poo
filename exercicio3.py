class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def informacao(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")


class Carro(Veiculo):
    def __init__(self, marca, modelo, numero_portas):
        super().__init__(marca, modelo)  
        self.numero_portas = numero_portas

    def informacao(self):
        super().informacao()  
        print(f"Número de portas: {self.numero_portas}")

meu_carro = Carro("Fiat", "Mobi ", 4) 
meu_carro.informacao()  


