num = int(input("Digite um número: "))
print(f"A tabuada de {num} é:")

for i in range(1,11):
    resultado = num * i
    print(f"{num} X {i} = {resultado}")
print()