lista = []
contador = 0

while contador < 10:
    produto = int(input("Digite um número: "))
    lista.append(produto)
    print("Número adicionado!")
    contador += 1

print(f"O maior número dessa lista é {max(lista)}")
print(f"O menor número dessa lista é {min(lista)}")
print(f"A média dessa lista é {sum(lista) / len(lista)}")