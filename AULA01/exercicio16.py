compras = []
contador = 0

while contador < 5:
    produto = input("Digite um produto para adicionar a lista de compras: ")
    compras.append(produto)
    print("Produto adicionado!")
    contador += 1

for i in compras:
    print(f"\n- {i}")
print()