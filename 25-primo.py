# Função para verificar se um número é primo
def eh_primo(numero):
    if numero <= 1:
      return False  # Números menores ou iguais a 1 não são primos
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False  # Se o número for divisível por i, não é primo
    return True  # Se não houver divisores, o número é primo

# Solicita um número ao usuário
num = int(input("Digite um numero: "))

# Verifica se o número é primo e exibe ao usuário
if eh_primo(num):
    print(f"{num} é um número primo.")
else:
    print(f"{num} não é um número primo")