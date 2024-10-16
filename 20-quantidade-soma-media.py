# Inicializando  variáveis
soma = 0
contador = 0

while True:
    # Lendo  um número inteiro digitado pelo usuário
    numero = int(input("Digite um número inteiro (0 para sair): "))

    # Verificando se o número é 0 para sair do loop
    if numero == 0:
        break

        #Atualizando a soma e o contador 
        soma += numero
        contador  += 1 

# Verificando  se algum numero foi digitado
if contador > 0:
    media = soma / contador
    print(f"Quantidade de números digitados: {contador}")
    print(f"Soma dos números: {soma}")
    print(f"Média aritmética: {media:.2f}")
else:
    print("Nenhum número foi digitado.")
    print("Fim do programa")  # Adicionei essa linha para finalizar o programa
