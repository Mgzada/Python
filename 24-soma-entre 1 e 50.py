# Algotimo para calcular  a soma dos números pares entre 1 a 50
soma_pares = 0
for numero in range(1,51):
    if numero % 2 == 0:
        soma_pares += numero

print(f"A soma dos números pares entre 1 e 50 é: {soma_pares}")