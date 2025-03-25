lass Cachorro:
    def _init_(self, nome, raca, comida, acordado=True):
        self.nome = nome
        self.raca = raca
        self.comida = comida  # Quantidade de comida disponível
        self.acordado = acordado
        self.feliz = False

    def comer(self, quantidade):
        if self.comida >= quantidade:
            self.comida -= quantidade
            self.feliz = True
            print(f"{self.nome} comeu {quantidade} unidades de comida e está feliz!")
        else:
            print(f"Não há comida suficiente para {self.nome}. Quantidade disponível: {self.comida}")

    def dormir(self):
        if not self.acordado:
            print(f"{self.nome} já está dormindo.")
        else:
            self.acordado = False
            print(f"{self.nome} foi dormir.")

    def brincar(self):
        if self.acordado:
            self.feliz = True
            print(f"{self.nome} brincou e está feliz!")
        else:
            print(f"{self.nome} está dormindo. Acorde-o para brincar!")

    def latir(self):
        if self.acordado:
            print(f"{self.nome} está latindo: Au Au!")
        else:
            print(f"{self.nome} está dormindo e não pode latir.")


# Instanciando dois cachorros com valores iniciais diferentes
cachorro1 = Cachorro(nome="Rex", raca="Labrador", comida=10)
cachorro2 = Cachorro(nome="Bella", raca="Poodle", comida=5, acordado=False)

# Interagindo com os cachorros
print("\n--- Interações com Rex ---")
cachorro1.latir()
cachorro1.brincar()
cachorro1.comer(3)
cachorro1.dormir()
cachorro1.latir()

print("\n--- Interações com Bella ---")
cachorro2.latir()       # Bella está dormindo
cachorro2.acordado = True  # Acordando Bella manualmente
print(f"{cachorro2.nome} acordou!")
cachorro2.latir()
cachorro2.comer(2)
cachorro2.brincar()
cachorro2.dormir()
