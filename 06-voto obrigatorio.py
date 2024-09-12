# Obrigatório: entre 18 anos e menores 65 anos.
# Opicional: entre 19 e 17 e a partir dos 65
# Não permitido: menores de 16 anos

print("Algoritmo do Voto Obrigatório")

idade = int(input("Digite a sua idade"))

if idade >= 18 and idade < 65:
    print("Voto Obrigatório!!!")
elif (16 <= idade < 18 or idade >= 65):
      print("Voto Opicional!!!")
else:
     print("Voto não permitido!!!")
     