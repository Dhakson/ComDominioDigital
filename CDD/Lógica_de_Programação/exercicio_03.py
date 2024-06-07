#Crie um algoritmo que leia o nome e duas notas do aluno e mostre na tela o nome e média desse alunos

nome = input('Nome do Aluno: ')

n1 = int(input('Primeira Nota: '))
n2 = int(input('Segunda Nota: '))

media = (n1 + n2) / 2

print(f"A media do {nome} é {media}")