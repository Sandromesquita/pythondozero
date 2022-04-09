sair = False
producao = 0

def librarMaquina(num_pecas, peso_pecas):
    global producao, peca_extra, peso_extra
    peso_total = num_pecas * peso_pecas
    if num_pecas <= 6 and peso_total <= 60:
        msn = "Maquina liberada!"
        producao = producao + 1
        peca_extra, peso_extra = 0, 0
    else:
        if num_pecas > 6:
            peca_extra = num_pecas - 6
            if peso_total > 60:
                peso_extra = peso_total - 60
            else:
                peso_extra = 0
        else:
            peca_extra = 0
            peso_extra = peso_total - 60

        msn = "Maquina Bloqueada!"

    return msn, producao, peca_extra, peso_extra

while True:
    conf = False

    num_pecas = int(input("Digite o numero de pecas: "))
    peso_pecas = float(input("Digite o peso de cada peca: "))

    msn, producao, peca_extra, peso_extra = librarMaquina(num_pecas, peso_pecas)

    print(msn)
    if peca_extra > 0:
        print("Devido excesso de pecas: ", peca_extra)
    if peso_extra > 0:
        print("Devido excesso de peso: ", peso_extra)

    while conf == False:
        cont = input("Deseja continuar a producao (s/n): ").lower()

        if cont == 's':
            conf = True
            continue
        elif cont == 'n':
            conf = True
            sair = True
        else:
            print("Opcao invalida!")

    if sair == True:
        break
    else:
        continue

print("="*20)
print("Producao encerrada!")
print(f'A maquina produziu {producao} ciclos de maquinas!')