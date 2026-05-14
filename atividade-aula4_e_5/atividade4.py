import random

alunos = int(input("Quantos alunos? "))

notas = []

for i in range(alunos):
    nota = random.randint(0, 10)
    notas.append(nota)

media = sum(notas) / alunos

igual = 0
acima = 0
abaixo = 0

for nota in notas:
    if nota == media:
        igual += 1
    elif nota > media:
        acima += 1
    else:
        abaixo += 1

print(notas)
print("Média da turma:", media)
print("Notas iguais à média:", igual)
print("Notas acima da média:", acima)
print("Notas abaixo da média:", abaixo)
