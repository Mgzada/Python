# Criando uma lista para armazenar os dados dos alunos
alunos = []

# Lendo o nome e a nota de 5 alunos 
for i in range(5):
    nome = input(f"Digite o nome do {i+1} º aluno: ")
    nota = float(input(f"Digite a nota de {nome}: "))
    alunos.append((nome, nota)) # Armazenando os dados como uma tupla (nome, nota)

# Exibindo o nome e a nota de cada aluno
print("\nNomes e notas de alunos: ")
for aluno in alunos:
    print(f"Aluno: {aluno[0]}, Nota: {aluno[1]}")