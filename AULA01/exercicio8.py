idade = int(input("Digite a idade da pessoa: "))

if idade >= 60:
    print("Essa pessoa é idosa")
elif idade >= 18:
    print("Essa pessoa é adulta")
elif idade >= 12:
    print("Essa pessoa é adolescente")
else:
    print("Essa pessoa é criança")