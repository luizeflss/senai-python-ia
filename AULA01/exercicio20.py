usuarios = []

while True:
    print("-------------------------")
    print("1 - Cadastrar usuarios")
    print("2 - Listar usuarios")
    print("3 - Buscar usuarios")
    print("4 - Remover  usuarios")
    print("5 - Sair")
    print("-------------------------")

    opcao = input("Escolha uma das opções: ")
    print()

    if opcao == "1":
        nome = input("Nome completo do usuario: ")
        idade = int(input("Idade do usuario:"))
        cidade = input("Cidade do usuario: ")

        novo_usuario = {"nome": nome, "idade": idade, "cidade": cidade}
        usuarios.append(novo_usuario)

    elif opcao == "2":
        if not usuarios:
            print("Nenhum usuario cadastrado.")
        else:
            print("Usuarios cadastrados:")
            for i, usuario in enumerate(usuarios):
                print(f"{i+1}. {usuario['nome']} - {usuario['idade']} anos - {usuario['cidade']}")
                print()
    elif opcao == "3":
        nome_busca = input("Digite o nome do usuario que deseja buscar: ")
        usuario_encontrado = None

        for usuario in usuarios:
            if usuario['nome'].lower() == nome_busca.lower():
                usuario_encontrado = usuario
                break

        if usuario_encontrado:
            print(f"Usuario encontrado: {usuario_encontrado['nome']} - {usuario_encontrado['idade']} anos - {usuario_encontrado['cidade']}")
        else:
            print("Usuario não encontrado.")

    elif opcao == "4":
        nome_remover = input("Digite o nome do usuario que deseja remover: ")
        usuario_remover = None

        for usuario in usuarios:
            if usuario['nome'].lower() == nome_remover.lower():
                usuario_remover = usuario
                break

        if usuario_remover:
            usuarios.remove(usuario_remover)
            print(f"Usuario {usuario_remover['nome']} removido com sucesso.")
        else:
            print("Usuario não encontrado.")

    elif opcao == "5":
        print("Encerrando o programa...")
        break   