from random import randint

frutas = [
(0, "Banana"), 
(1, "Maçã"),
(2, "Uva"),
(3, "Limão"),
(4, "Pera"),
(5, "Mamão"),
(6, "Melancia"),
(7, "Caju"),]

resultado = []
res = 0
#Sorteia as frutas
for i in range(4):
    num = randint(0,7)
    for x, fruta in frutas:
        if x == num:
            resultado.append(fruta)
print(resultado)

#Procura a Fruta que mais se repete
for x in range(4):
    contador = resultado.count(resultado[x])
    if contador > res:
        res = contador
        
#Imprime o resultado de acordo com a regra
if res == 4:
    print("Maximo 4 Acertos")
elif res == 3:
    print("Medio 3 Acertos")
elif res == 2:
    print("Minimo 2 Acertos")
else:
    print("Tente Outra Vez")
        
    

