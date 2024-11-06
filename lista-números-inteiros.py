# Crie uma lista de 5 números inteiros fornecidos pelo usuário imprima o maior, o menor e a soma de todos os elementos
numeros = []

for i in range(5):
    num = int(input(f"Digite o {i+1} º número inteiro: "))
    numeros.append(num)

# Calculando o maior, o menor e a soma dos elementos
maior = max(numeros)
menor = min(numeros)
soma = sum(numeros)

# Imprimindo os resultados
print(f"O maior numero é: {maior}")
print(f"O menor numero é: {menor}")
print(f"A soma dos numeros é: {soma}")
