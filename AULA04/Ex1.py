# Lista de Exercícios — Primeiros Passos com IA em Python (NVIDIA API)
# Exercício 1 — Primeira Pergunta para a IA
# Crie um programa que:
# faça uma pergunta usando input()
# envie para a IA
# mostre a resposta na tela

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

pergunta = input("Digite a sua pergunta para a IA:\n")

resposta = cliente.chat.completions.create(
    model="meta/llama-3.1-8b-instruct",

    messages=[
        {
            "role": "system",
            "content": "Você é um assistente inteligente."
        },

        {
            "role": "user",
            "content": pergunta
        }
    ]
)
print("\nResposta da IA:\n")
print(resposta.choices[0].message.content)