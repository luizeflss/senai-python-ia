# Exercício 6 — Explicador de Palavras
# Faça uma IA que:
# receba uma palavra
# explique o significado de forma simples
# Exemplo:
# “algoritmo”
# “internet”
# “inteligência artificial”

# Resposta no fim do arquivo

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

print("DIgite 'sair' para fechar o programa")
while True:
    palavra = input("\nDigite a palavra que deseja saber o significado: \n")
    if palavra.lower() == "sair" :
        print("Programa Encerrado")
        break

    resposta = cliente.chat.completions.create(
        model="meta/llama-3.1-8b-instruct",

        messages=[
            {
                "role": "system",
                "content": "Você é um especialista em siginificados das palavras, vc sempre entrega a explicação das palavras solicitadas de maneira breve"
            },

            {
                "role": "user",
                "content": palavra
            }
        ]
    )

    print("Tradução da IA:")
    print(resposta.choices[0].message.content)

# Neste exercicio a capacidade dela expressar o significado da palvra está correto, eu ainda exigi que ele fizesse
# coisas curtas para não ter problema com um texto gigante e ainda assim ficou bem claro todos os significados solicitados e os que eu pedi
