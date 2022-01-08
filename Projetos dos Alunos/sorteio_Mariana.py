import random
lista = ['maçã', 'uva', 'goiaba', 'banana']
#Defina uma função que cria para ordenar o peso

def peso () :
  return random.random()

random.shuffle(lista,peso)
print(lista)