num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    print(f"{num1} é o maior número.")
elif num1 < num2:
    print(f"{num2} é o maior número.")
else:
    print("Os números são iguais.")