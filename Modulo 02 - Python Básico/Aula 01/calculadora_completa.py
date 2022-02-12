def calcular(a, op, b):
    if op == '+':
        resultado = a + b

    elif op == '-':
        resultado = a - b

    elif op == 'X':
        resultado = a * b

    elif op == '/':
        resultado = a / b

    return resultado

def teclado():
    num1 = float(input("Digite um numero: "))
    op = input("Digite a operação desejada ( + , - , x , / ): ")

    while op != '+' and op != '-' and op != 'x' and op != '/' and op != 'X':
        op = input("Digite a operação desejada ( + , - , x , / ): ")

    num2 = float(input("Digite outro numero: "))

    if op == 'x':
        op = op.upper()

    elif op == '/':
        while num2 == 0:
            num2 = float(input("Digite um numero diferente de zero: "))

    return num1, op, num2

print("="*20,"CALCULADORA PYTHON","="*20)

while True:
    num1, op, num2 = teclado()

    resultado = calcular(num1, op, num2)
    print("O resultado é {} ".format(resultado))

    print("=" * 80)
    cont = input("Deseja fazer outra conta? (s/n) ").upper()
    print("=" * 80)
    if cont == "N":
        break

print("")
print("=" * 80)
print("=" * 21,"Obrigado por usar nossa calculadora!", "=" * 21)
print("=" * 80)