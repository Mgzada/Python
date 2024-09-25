  # Atividade 08-tabuada.py
  # Faça um progama que mostre a tabuada de um número que o 

contador = 0
multiplicador = int(input("Digite o valor do multiplicador"))
resultado = 0


while contador <= 10:
   resultado = multiplicador * contador
   print(multiplicador, " x ", contador, " = ", resultado)
   print(f"{multiplicador} x {contador} = {resultado}")
   contador += 1
   