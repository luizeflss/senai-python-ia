# Exercício 8 — Chat Motivacional
# Faça uma IA que:
# aja como treinador motivacional
# dê mensagens positivas para o usuário
# O usuário pode digitar:
# “Estou cansado”
# “Preciso estudar”
# “Estou sem ideias”

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
    "aja como treinador motivacional"
)
print("--DIgite 'sair' para fechar o programa--")
print("\nMe diga como vc esta se sentido hoje:")
while True:
    palavra = input("\nR: \n")
    if palavra.lower() == "sair" :
        print("Programa Encerrado")
        break

    resposta = cliente.chat.completions.create(
        model="meta/llama-3.1-8b-instruct",

        messages=[
            {
                "role": "system",
                "content": personalidade
            },

            {
                "role": "user",
                "content": palavra
            }
        ]
    )

    print("IA couch:")
    print(resposta.choices[0].message.content)

# achei interresante as resposta ele realmente agiu como um couch, e ainda armazenou dados das minhas resposta anteriores com dominio