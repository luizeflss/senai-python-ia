num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
print("\nOPERADORES: " \
"\n Soma: +" \
"\n Subtração: -" \
"\n MUltiplicaçao: *" \
"\n Divisão: /")
operador = input("Esolha um operador: ")
print("")

def calcular (num1, num2, operador):
    if operador == "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operador == "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    elif operador == "*":
        print(f"{num1} X {num2} = {num1 * num2}")
    elif operador == "/":
        if num2 == 0 :
            print("Não possivel dividir por zero")
        else:
            print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Opção inválida")

calcular(num1, num2, operador)