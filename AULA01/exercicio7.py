num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
print("OPERADORES:" \
"\n1) Soma" \
"\n2) Subtração" \
"\n3) MUltiplicação" \
"\n4) Divisão")
op = input("Digite o núemro do operador: ")

match op:
    case "1":
        print(f"{num1} + {num2} = {num1+num2}")
    case "2":
        print(f"{num1} - {num2} = {num1-num2}")
    case "3":
        print(f"{num1} * {num2} = {num1*num2}")
    case "4":
        if num2 <= 0:
            print("Não possível dividir por zero")
        else:
            print(f"{num1} / {num2} = {num1/num2}")