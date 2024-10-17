# Algoritmo para exibir a tabuada de um número fornecido pelo usuário
numero = int(input("Digite o número para ver sua tabuada: "))

print(f"Tabuada do {numero}:")
for i in range (1, 11):
    resultado = numero * i 
    print(f"{numero} x {i} = {resultado}")
    