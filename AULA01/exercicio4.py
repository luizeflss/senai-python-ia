nota1 = int(input("Digite a primeira nota do aluno: "))
nota2 = int(input("Digite a segunda nota do aluno: "))
nota3 = int(input("Digite a terceira nota do aluno: "))

notaAluno = (nota1 + nota2 + nota3) / 3
print(f"A nota desse aluno é de {notaAluno:.2}")

if notaAluno >= 9:
    print("Aluno aprovado com exelencia!")
elif notaAluno >= 7:
    print("Aluno Aprovado")
elif notaAluno >= 5:
    print("Aluno em recuperação!")
else:
    print("Aluno reprovado!")