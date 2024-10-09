# Utiliza estrutura de repetição para exibir a sequência
for i in range(1, 101):
    if i == 6:
        print("Não vou mostrar o 6")
        continue
    elif 10 <= i <= 27:
        print(f"Não mostrar o número {i}")
        continue
    elif i == 40:
        print(i)
        break
    else:
        print(i)

print("Acabou")