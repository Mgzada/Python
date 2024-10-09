 # Ferramenta Continue
 # A ferramenta continue no python vai interromper o loop,
 # mas vai dar continuidade a ele.

contador = 0

while contador <= 40:
    contador += 1

    # Verifica se o valor de 'contador' é multiplo de 4
    if contador % 4 == 0:
        print("pim") # Se for múltiplo de 4, imprime "pim"
        continue # Interrompe a interação atual e volta para o inicio do loop

    # Se o número não for múltiplo de 4, imprime o valor do contador
    print(contador)
# Após o termino de loop, imprime a mensagem de finalização
print("Fim do progama")
