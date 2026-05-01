from bokeh.palettes import Oranges9

lista_frutas = ["Morango", "Maça", "Uva"]
# Lista frutas[0] = "Morango"
# Lista frutas[1] = "Maça"
# Lista frutas[2] = "Uva"
print(lista_frutas)

lista_frutas.append("Melancia")
print(lista_frutas[3])

for i in range(len(lista_frutas)):
     print(lista_frutas[i])

for fruta in lista_frutas:
    print(fruta)