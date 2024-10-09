 # Ferramenta Break
 # É uma ferramenta pra interromper e necerrar um loop 
 # Isso quer dizer que vamos parar o loop naquele momento e vamos sair dele.
 # Execute o código abaixo e explique o que ele faz

while True: 
    nome = input('Digite o seu nome ou escreva "sair":')

    if nome == 'sair':
        break # para a execução do while, sai do loop de repetição

    print(f'Seu nome é {nome}')

print('Acabou')
