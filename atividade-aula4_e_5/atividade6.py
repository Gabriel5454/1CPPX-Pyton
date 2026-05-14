import random

n = int(input("digite o tamanho do vetor: "))

vetor = []

for i in range(n):
    numero = random.randint(0,100)
    vetor.append(numero)
soma = sum(vetor)
print(vetor)
print(f"a soma dos numeros dentro do vetor: {soma}")
