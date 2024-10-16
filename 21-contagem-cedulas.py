# Solicita um valor inteiro positivo ao usuário
valor = int(input("Digite um valor inteiro positivo para pagamento: "))

# Verifica se o valor é positivo
if valor < 0:
    print("Por favor, digite um valor positivo.")
else:
    # Inicializando a quantidade de cédulas
    cedulas_50 = cedulas_20 = cedulas_10 = cedulas_5 = cedulas_1 = 0

    # Cálculo das cédulas
    while valor > 0:
        if valor >= 50:
            cedulas_50 += valor // 50
            valor %= 50
        elif valor >= 20:
            cedulas_20 += valor // 20
            valor %= 20
        elif valor >= 10:
            cedulas_10 += valor // 10
            valor %= 10
        elif valor >= 5:
            cedulas_5 += valor // 5
            valor %= 5
        else:
            cedulas_1 += valor // 1
            valor %= 1

    # Exibindo a quantidade de cédulas utilizadas
    print(f"Cédulas de R$ 50: {cedulas_50}")
    print(f"Cédulas de R$ 20: {cedulas_20}")
    print(f"Cédulas de R$ 10: {cedulas_10}")
    print(f"Cédulas de R$ 5: {cedulas_5}")
    print(f"Cédulas de R$ 1: {cedulas_1}")