contador = 0
somaNum = 0
while contador < 5:
    num = int(input("Digite um números: "))
    somaNum += num
    contador += 1
    print("Número adicionado a soma!")
print(f"A soma total é: {somaNum}")