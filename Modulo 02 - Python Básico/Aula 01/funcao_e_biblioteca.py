import turtle

def desenhar(ang, tam, qtd_lados):
    for i in range(qtd_lados):
        desenhista.forward(tam)
        desenhista.left(ang)

num_lados = int(input("Digite o numero de lados: "))
tam_lado = int(input("Digite o tamanho do lado: "))
angulo = 360/num_lados

tela = turtle.Screen()
tela.bgcolor("green")

desenhista = turtle.Turtle()

desenhar(angulo, 100, num_lados)


tela.exitonclick()
