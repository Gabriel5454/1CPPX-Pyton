
for n in range(2, 2001):
    divisores = 0

    for i in range(1, n + 1):
      if n % i == 0:
          divisores += 1

    if divisores == 2:
      print(n)