def calcular(a, op, b):
    if op == '+':
        resultado = a + b

    elif op == '-':
        resultado = a - b

    elif op == 'x':
        resultado = a * b

    elif op == '/':
        resultado = a / b

    else:
        print("Operação inválida")

    return resultado

num1 = float(input("Digite um numero: "))
op = input("Digite a operação desejada ( + , - , x , / ): ")
if op == '/':
    num2 = float(input("Digite outro numero: "))
    while num2 == 0:
        num2 = float(input("Digite um numero diferente de zero: "))

resultado = calcular(num1, op, num2)
print("O resultado é: ", resultado)