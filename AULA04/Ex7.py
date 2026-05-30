# Exercício 7 — Quiz com IA
# Crie um programa onde:
# a IA cria uma pergunta de conhecimentos gerais
# o aluno responde
# a IA diz se parece correta ou não

# Corrigir essa bomba

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("Erro: A variável API_KEY não foi encontrada. Verifique se o arquivo .env está na raiz do projeto.")

cliente = OpenAI(
    api_key=API_KEY,
    base_url="https://integrate.api.nvidia.com/v1"
)

personalidade =(
    "aja como um professor de conhecimentos gerais e vc é bem rigido, que monta quiz para seus alunos "
)
print("--DIgite 'sair' para fechar o programa--")
print("\nBora começar esse Quiz:")

while True:
    palavra = input("\nR: \n")
    if palavra.lower() == "sair" or palavra.lower()=="não" or palavra.lower()=="nao" :
        print("Programa Encerrado")
        break

    resposta = cliente.chat.completions.create(
        model="meta/llama-3.1-8b-instruct",

        messages=[
            {
                "role": "system",
                "content": personalidade + "Lembre-se de sempre avisar o usuario se ele acertou ou errou a questão e caso erre apenas alerte e prossiga para a proxima questão"+
                "e reconheca as letras das alternativas quando vc estiver esperando uma resposta"+"Voce não liga para respostas sem acento vc entende oq o usuario quer dizer"
            },

            {
                "role": "user",
                "content": palavra
            }
        ]
    )

    print("IA teacher:")
    print(resposta.choices[0].message.content)
