################ALUNOS INVOLVIDOS NO PROJETO#####################
# MATRICULA - 20192113862 - NOME - MATHEUS GUSTAVO PEREIRA      #
# MATRICULA - 20192113816 - NOME - RAFAEL DE OLIVEIRA MACHADO   #
#################################################################

import random
from datetime import datetime

class Sorteio:
    def __init__(self):
        ###########VARIAVEIS##########
        self.running = True
        self.start = ''
        self.invalidSaldo = True
        self.invalidAposta = True
        self.modo = ''
        self.modoJogo = ''
        self.numeroSorteado = 0
        # voce pode adicionar mais frutas a lista caso queira.
        self.frutas = ['Laranja', 'Limão', 'Manga', 'Banana', 'Melão', 'Abacate', 'Uva', 'Maçã', 'Pitomba', 'Acerola',
                  'Goiaba',
                  'Siriguela', 'Cajá', 'Cupuaçu', 'Pera', 'Jabuticaba', 'Caju', 'Tangerina', 'Framboesa', 'Açaí',
                  'Amora',
                  'Araticum',
                  'Bacaba', 'Biribá', 'Cacau', 'Caqui', 'Carambola', 'Cereja', 'Coco', 'Cupuaçu', 'Figo', 'Groselha',
                  'Jaca', 'Kiwi', 'Maracujá']
        self.frutasArray = []
        self.frutasSorteadas = []
        self.saldo = 0
        self.saldoInicial = 0
        self.saldoComDeposito = 0
        self.saldoFinal = 0
        self.valorDeposito = 0
        self.aposta = 0
        self.userName = ''
        self.continuar = ''
        self.sortear = 's'
        self.historico = []


    ############FUNÇÕES#############
    # mostra o cabecalho
    def cabecalho(self):
        print('################## JOGO DAS FRUTAS SORTEIO ########################')
        print('Sorteio das frutas, são 3 modos diferentes(com 6 ,8 ou 12 frutas)')
        print('Serão sorteadas 4 frutas,os tipos de prêmio são:')
        print('1- MAIOR PRÊMIO (as 4 frutas iguais), valor da aposta x 10')
        print('2- (as 2 primeiras frutas iguais) e (as 2 últimas frutas iguai) valor da aposta x 05')
        print('3- (Todas as frutas diferentes) valor da aposta x 02')
        print('Qualquer outa combinação o jogador perderá o valor apostado')
        print('#####################################################################')

    # pega o modo de jogo escolhido e processa o array de frutas
    def getModoJogo(self):
        if self.modo == '1':
            self.modoJogo = 'MODO-1'
            for x in self.frutas:
                index = random.randint(0, len(self.frutas) - 1)
                # if frutas[index] not in frutasArray:
                self.frutasArray.append(self.frutas[index])
                if len(self.frutasArray) == 6: break
        elif self.modo == '2':
            self.modoJogo = 'MODO-2'
            for x in self.frutas:
                index = random.randint(0, len(self.frutas) - 1)
                # if frutas[index] not in frutasArray:
                self.frutasArray.append(self.frutas[index])
                if len(self.frutasArray) == 8: break
        else:
            self.modoJogo = 'MODO-3'
            for x in self.frutas:
                index = random.randint(0, len(self.frutas) - 1)
                # if frutas[index] not in frutasArray:
                self.frutasArray.append(self.frutas[index])
                if len(self.frutasArray) == 12: break

    # checa se o saldo é maior q zero
    def checaSaldo(self):
        if self.saldo > 0 or self.saldo == '':
            return True
        else:
            return False

    # checa se a aposta é maior que zero
    def checaApostaIsValid(self):
        if self.aposta > 0 or self.aposta == '':
            return True
        else:
            return False

    # checa se a aposta é menor ou igual o saldo
    def checaApostaMaiorQueSaldo(self):
        if self.aposta <= self.saldo:
            return True
        else:
            return False

    # faz o sorteio das frutas
    def sortearFrutas(self):
        for x in range(0, 4):
            self.numeroSorteado = random.randint(0, len(self.frutasArray) - 1)
            self.frutasSorteadas.append(self.frutasArray[self.numeroSorteado])

    # mostra o resultado final na tela
    def showResultado(self,text):
        print(text)

    # mostra todas as apostas feitas pelo usuario
    def setHistorico(self,value):
        self.historico.append(value)

    # mostra o resultado final  quando o jogo acaba
    def showResultadoFinal(self):
        print('#####################################################################')
        print('# RECIBO DAS APOSTAS Data ' + datetime.today().strftime('%d-%m-%Y'))
        print('# Usuário : ' + str(self.userName))
        print('# Saldo Inicial : R$' + str(self.saldoInicial))
        for x in range(0, len(self.historico) ):
            print('# ' + self.historico[x])

        print('# Saldo Final : R$' + str(self.saldoFinal))
        result = self.saldoFinal - self.saldoComDeposito
        print('# Ganho/Perda final = R$' + str(result))
        print('#####################################################################')

    #checa se o valor é numero
    def isNumber(self,value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    #inicia o sorteio
    def startGame(self):
        ###########INICIO###########
        self.cabecalho()
        self.userName = input('Insira o seu nome por favor: ')
        while self.modo != '1' and self.modo != '2' and self.modo != '3':
            print('Escolha o MODO de JOGO: MODO-1(6 FRUTAS),MODO-2(8 FRUTAS),MODO-3(12 FRUTAS) ')
            self.modo = input('1(MODO-1), 2(MODO-2), 3(MODO-3) :')

        self.getModoJogo()

        while self.sortear.lower() != 'n':
            print('Frutas em jogo : ' + str(self.frutasArray) + ' Modo do jogo :' + self.modoJogo)
            self.sortear = input('Deseja sortear novamente as frutas?: (s/n) ')
            if self.sortear.lower() == 's':
                self.frutasArray.clear()
                self.getModoJogo()



        while self.invalidSaldo:
            self.saldo = input('Insira o seu saldo por favor: ').replace(',', '.')
            if self.isNumber(self.saldo):
                self.saldo = float(self.saldo)
                if self.checaSaldo():
                    self.saldo = self.saldo - self.aposta
                    self.saldoInicial = self.saldo
                    self.saldoComDeposito = self.saldo
                    self.invalidSaldo = False
                else:
                    print('Saldo não pode ser menor ou igual a zero')
            else:
                self.invalidSaldo = True
                print('Por favor digite um número,apenas números são permitidos.')

        while self.running:

            print('SALDO ATUAL :' + str(self.saldo))
            while self.invalidAposta:
                self.aposta = input('Insira a aposta por favor: ').replace(',', '.')
                if self.isNumber(self.aposta):
                    self.aposta = float(self.aposta)
                    if self.checaApostaIsValid():
                        if self.checaApostaMaiorQueSaldo():
                            self.saldo = self.saldo - self.aposta
                            self.invalidAposta = False
                            print('Valor da aposta R$ ' + str(self.aposta))
                            print('Seu Saldo atual ficará : R$' + str(self.saldo))
                        else:
                            print('O valor da aposta não pode ser maior que o saldo : R$ ' + str(self.saldo))

                    else:
                        print('Aposta não pode ser menor ou igual a zero')
                else:
                    self.invalidAposta = True
                    print('Por favor digite um número,apenas números são permitidos.')

            self.start = input('Deseja Iniciar a aposta: (s/n) ')
            print('#####################################################################')

            if self.start.lower() == 's' or self.start.lower() != 'n':
                if self.start.lower() != 'n':
                    print('Qualquer tecla digitada, continuando a aposta...')
                self.sortearFrutas()
                print(self.frutasSorteadas)
                if len(self.frutasSorteadas) > 0:
                    if self.frutasSorteadas[0] == self.frutasSorteadas[1] and self.frutasSorteadas[0] == self.frutasSorteadas[2] and  self.frutasSorteadas[0] == self.frutasSorteadas[3]:
                        premio = self.aposta * 10
                        self.saldo = self.saldo + self.premio
                        self.showResultado(
                            "PARABÉNS Todas as frutas são iguais, aposta multiplicada por x10, VALOR RECEBIDO = R$" + str(
                                premio))

                    elif self.frutasSorteadas[0] == self.frutasSorteadas[1] and self.frutasSorteadas[2] == self.frutasSorteadas[3]:
                        premio = self.aposta * 5
                        self.saldo = self.saldo + premio
                        self.showResultado(
                            "QUAAAASE, As duas primeiras frutas são iguais e as duas últimas são iguais, aposta multiplicada por x5, VALOR RECEBIDO = R$" + str(
                                premio))

                    elif len(set(self.frutasSorteadas)) == len(self.frutasSorteadas):
                        premio = self.aposta * 2
                        self.saldo = self.saldo + premio
                        self.showResultado(
                            "Leegal, todas as frutas são diferentes, aposta multiplicada por x2 VALOR RECEBIDO = R$" + str(
                                premio))
                    else:
                        self.showResultado('QUE PENA, voce perdeu, VALOR PERDIDO = R$' + str(self.aposta))

            elif self.start.lower() == 'n':
                self.running = False
                self.saldo = self.saldo + self.aposta
                self.saldoFinal = self.saldo
                self.aposta = 0

            print('Última aposta :R$' + str(self.aposta) + ' ,saldo após aposta : R$' + str(self.saldo))
            self.setHistorico('Aposta :R$' + str(self.aposta) + ' ,saldo após aposta : R$' + str(self.saldo))
            if self.saldo == 0:
                print('QUE PENA SEU SALDO ACABOU ')
                result = input('Seu saldo está zerado, Deseja fazer um deposito: (s/n) ')

                if result == 's':
                    self.valorDeposito = input('Digite o valor do deposito : ')
                    self.saldo = self.saldo + float(self.valorDeposito)
                    self.saldoComDeposito = self.saldoComDeposito + float(self.valorDeposito)
                    self.setHistorico('Deposito efetuado no valor de R$' + str(self.valorDeposito))

            self.continuar = input('Deseja continuar apostando: (s/n) ')

            self.invalidSaldo = True
            self.invalidAposta = True
            self.frutasSorteadas.clear()

            if self.continuar.lower() == 's':
                self.running = True
            elif self.continuar.lower() == 'n':
                self.saldoFinal = self.saldo
                self.showResultadoFinal()
                fechar = input('Aperta alguma tecla para sair do sorteio ')
                self.running = False
            else:
                print('Qualquer tecla digitada, continuando a aposta...')
                self.running = True


#############################################################################

#instancia objeto
jogo = Sorteio()
#inicio o sorteio
jogo.startGame()
