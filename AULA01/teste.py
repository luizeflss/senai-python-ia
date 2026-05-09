mensagem = "Hello Word"
print(mensagem)

#USO DO IF E ELSE PARA VALIDAÇÃO DE NOTA DE ALUNO
notaAluno = int(input("Digite a nota do aluno: "))

if notaAluno >= 9:
    print("Aluno aprovado com exelencia!")
elif notaAluno >= 7:
    print("Aluno Aprovado")
elif notaAluno >= 5:
    print("Aluno em recuperação!")
else:
    print("Aluno reprovado!")


for num in range(1, (10+1)):
    print(num)

compras = ["bolo", "coca", "coxinha", "agua"]
for indice, item in enumerate(compras):
    print(f"na posição {indice + 1}, nos temos {item}")

segundos = 5

while segundos > 0:
    print(f"Faltam {segundos} segundos para o lançamento...")
    segundos-=1
print("Decolando...")

senhaCorreta ="12345"
senhaDigitada = ""

while senhaDigitada != senhaCorreta:
    senhaDigitada = input("Digite a senha: ")
    if senhaDigitada == senhaCorreta:
        print("Acesso liberado!")
    else:
        print("senha incorreta")
print("")