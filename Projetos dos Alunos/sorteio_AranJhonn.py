import random

lista_frutas = ["Maçã", "Pera", "Uva", "Banana", "Abacate", "Abacaxi", "Laranja", "Melão"]
lista_sorteio = []

print("Fruta da sorte:", lista_frutas[0])
for i in range(0, 4):
    sorteio = lista_frutas[random.randrange(0, 7)]
    lista_sorteio.append(sorteio)
    if sorteio == lista_frutas[0]:
        print("Sorteio num:", i+1, "", sorteio,"-> Ganhou o prêmio maximo!")
    else:
        print("Sorteio num:", i+1, "",sorteio)

print("")
if lista_sorteio[0] == lista_sorteio[1] and lista_sorteio[2] == lista_sorteio[3]:
    print("Lista sorteada:", lista_sorteio)
    print("Ganhou o prêmio medio!")
else:
    print("Lista sorteada:", lista_sorteio)
    print("Não ganhou nada! Tente novamente.")

