senhaCorreta ="12345"
senhaDigitada = ""

while senhaDigitada != senhaCorreta:
    senhaDigitada = input("Digite a senha: ")
    if senhaDigitada == senhaCorreta:
        print("Acesso liberado!")
    else:
        print("senha incorreta")
print("")