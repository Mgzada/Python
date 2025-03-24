class Produto:
    def __init__(self, nome, preco, quantidade):
        self.__nome = nome
        self.__preco = preco
        self.quantidade = quantidade
   
    # Getter para o nome
    @property
    def nome(self):
        return self.__nome
    
    # Getter para o preco
    @property
    def preco(self):
        return self.__preco
    
    #   Setter para o preço com validação 
    @preco.setter
    def preco(self, valor):
        if valor < 0:
            raise ValueError("O preço não pode ser negativo")
        self.__preco = valor
        
 # Instanciando um objeto Produto e testando os métodos
    if __name__ == "__main__":
    # Criando um produto
        produto = Produto ("Camiseta", 29.90, 10) # type: ignore

        # Acessando os atributos
        print(f"Nome: {produto.nome}")
        print(f"Preço: R${produto.preco:.2f}")
        print(f"Quantidade: {produto.quantidade}")

        #Testando o setter de preço
        try:
            produto.preco = -15.00  # Tentativa de definir um preço negativo
        except ValueError as e:
            print(e) # Exibindo a mensagem de erro

        #Definindo um preço valido 
        produto.preco = 25.00
        print(f"Novo preço: R${produto.preco:.3f}")