num = int(input("Digite um numero: "))

print(f" Os divisores de {num} são :")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)