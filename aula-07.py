# IMC
# Ler peso e altura
# Calcule o IMC

print("IMC")
peso = float(input("Peso(kg): "))
altura = float(input("Altura(m): "))
imc = peso / (altura ** 2)

print(f"Seu IMC é {imc: .2f}") # .2f é usado
# para mostrar apenas duas casas decimais. 

if (imc < 18.5):
    print("Abaixo do peso")
elif (18.5 <= imc <25):
    print("Peso normal")
elif (25 <= imc <30):
    print("Sobrepeso")
else:
    print("Obesidade")  # else é usado para o último caso.  # O