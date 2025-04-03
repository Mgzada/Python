class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0, limite=0):
        self.__titular = titular
        self.__saldo = saldo_inicial
        self.__limite = limite

    def depositar(self, valor): 
        if valor > 0:
            self.__saldo += valor
            print(f'Depósito de R${valor:.2f} realizado com sucesso.')
        else:
            print('Valor de depósito deve ser positivo.')

    def sacar(self, valor):
        if valor > 0 and valor < (self.__saldo + self.__limite):
            self.__saldo -= valor
            print(f'Saque de R${valor:.2f} realizado com sucesso.')
        else:
            print('Saque não permitido. Verifique o saldo e o limite.')

    def get_saldo(self):
        return self.__saldo
    
    def set_limite(self, novo_limite):
        if novo_limite > 0:
            self.__limite = novo_limite
            print(f'Limite alterado para R${novo_limite:.2f}.')
        else:
            print('O limite deve ser um valor não negativo.')

#Exemplo de uso
if __name__ == "__main__":
    conta = ContaBancaria("João", 1000, 500)
    conta.depositar(200)
    print(f'Saldo atual: R${conta.get_saldo():.2f}')
    conta.sacar(1200)
    print(f'Saldo atual: R${conta.get_saldo():.2f}')
    conta.set_limite(1000)
    conta.sacar(1200)
    print(f'Saldo atual: R${conta.get_saldo():.2f}')
