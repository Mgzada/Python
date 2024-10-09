# Definição das funções

# Função exibir menu
def exibirMenu():
    print("CALCULADORA DAS OPERAÇÔES BÁSICAS:")
    print("Menu de escolha")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5. Resto da Divisão")
    print("6. Sair")
    escolha = int(input("Escolha uma opção"))
    return escolha


    def soma(n1, n2):
        return n1 + n2
    

    def subtracao(n1, n2):
        return n1 - n2
    

    def multiplicacao(n1, n2):
        return n1 * n2
    

    def divisao(n1, n2):
        if n2 != 0:
            return n1 / n2 
        else:
            return "Erro: Divisão por zero não é permitida."
        

    def resto_divisao(n1, n2):
        if n2 != 0:
            return n1 % n2 
        else: 
            return "Erro: Divisão por zero não é permitida."
        

 # Declaração de variáveis
opcao = 0
n1 = 0
n2 = 0

# Início de código
while opcao != 6:
    opcao = exibirMenu()

    if opcao in [1, 2, 3, 4, 5]:
        n1 = float(input("Insira o primeiro valor"))
        n2 = float(input("Insira o segundo valor:"))

    if opcao == 1:
        print(f"A soma dos valores é: {soma (n1, n2)}\n")
    elif opcao == 2:
        print(f"A subtração dos valores é: {subtração(n1, n2)}\n")
    elif opcao == 3:
        print(f"A multiplicação dos valores é: {multiplicação(n1, n2)}\n")
    elif opcao == 4:
        print(f"A divisão dos valores é: {divisão(n1, n2)}\n")
    elif opcao == 5:
        print(f"O resto da divisão dos valores é: {resto_divisão(n1, n2)}\n")
    elif opcao == 6:
        print("Finalizando o código!")
    else:
        print("Opção inválida. Tente novamente. \n")