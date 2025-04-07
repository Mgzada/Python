class Veiculo:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano
        
    def info(self):
        return f'Modelo: {self.modelo}, Ano: {self.ano}'
        
class Carro(Veiculo):
    def __init__(self, modelo, ano, numero_de_portas):
        super().__init__(modelo, ano) # Chama o construtor da classe pai
        self. numero_de_portas = numero_de_portas
        
    def info(self):
        return f'{super().info}, Número de portas: {self.numero_de_portas}'
        
    def ligar_ar_condicionado(self):
        return f'0 ar condicionado do {self.modelo} está ligado'
        
class Moto(Veiculo):
    def __init__(self, modelo, ano, tipo):
        super().__init__(modelo, ano) # Chama o construtor da classe pai
        self.tipo = tipo 
        
    def info(self):
        return f'{super().info()}, Tipo: {self.tipo}'
        
    def empinar(self):
        return f'{super().info()}, Tipo: {self.tipo}'
        
# Exemplo de uso
carro = Carro("Fusca", 1970, 2)
print(carro.info())
print(carro.ligar_ar_condicionado())

moto = Moto ("Harley Davidson", 2020, "Cruiser")
print(moto.info())
print(moto.empinar())