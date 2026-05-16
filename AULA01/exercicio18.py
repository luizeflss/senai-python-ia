nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
cidade = input("Digite a cidade: ")

Perfil = {
    "Nome": nome,
    "Idade": idade,
    "Cidade": cidade,
}

print("\nCadastro:")
print(f"Nome: {Perfil['Nome']}")
print(f"Idade: {Perfil['Idade']}")
print(f"Cidade: {Perfil['Cidade']}")
print()
