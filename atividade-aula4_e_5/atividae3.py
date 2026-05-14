import random
from random import Random

num = int(input("Digite o numero: "))

vetor = []
for i in range(num):
    num = random.uniform(0,100)
    vetor.append(num)

print("Numeros gerados:")

for num in vetor:
     print(num)
