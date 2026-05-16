numeros = []

for i in range(5):
    numero = int(input(f"Digite o número: "))
    numeros.append(numero)

set_numeros = set(numeros)

print("Numeros sem duplicados:", set_numeros)