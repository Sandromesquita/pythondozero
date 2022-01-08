import random

frutas = ["lichia", "abacaxi", "morango", "melancia", "amora", "manga", "melao", "laranja"]
sorteio_frutas = []

x = 0
for x in range(4):
    sorteio_frutas.append(random.choice(frutas))

print(sorteio_frutas)

Premio_Max = sorteio_frutas[0] == sorteio_frutas[1] == sorteio_frutas[2] == sorteio_frutas[3]
Premio_Med = sorteio_frutas[0] == sorteio_frutas[1] or sorteio_frutas[2] == sorteio_frutas[3]

if (Premio_Max == True):
    print("Prêmio Máximo")

elif (Premio_Med == True):
    print("Prêmio Médio")

else:
    print("Nenhuma Premiação!")