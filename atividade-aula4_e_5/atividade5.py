mes = [
    "Jan", "Fev", "Mar", "Abr",
    "Mai", "Jun", "Jul", "Ago",
    "Set", "Out", "Nov", "Dez"
]

dia = [
    31, 28, 31, 30,
    31, 30, 31, 31,
    30, 31, 30, 31
]

for i in range(12):
    print(f"O Mês de {mes[i]} tem {dia[i]} ao todo" )