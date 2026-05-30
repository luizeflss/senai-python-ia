# Exercício 4 — Gerador de Histórias
# Faça um programa que:
# peça o nome de um personagem
# peça um tema
# gere uma pequena história usando a IA
# Exemplo:
# personagem: Ana
# tema: espaço

# Resposta no fim do Arquivo

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

nome_personagem = input("Digite o nome do personagem:\n")
tema = input("Digite o tema da história:\n")

resposta = cliente.chat.completions.create(
    model="meta/llama-3.1-8b-instruct",

    messages=[
        {
            "role": "system",
            "content": (
                f"Você é um contador de histórias criativo e envolvente. "
                f"Crie uma história curta e cativante com o personagem {nome_personagem} "
                f"e o tema {tema}."
            )
        }
    ]
)
print("\nHistória gerada:\n")
print(resposta.choices[0].message.content)

# Resposta:
# O resultado da historia e bom, porem eu senti que ele esta se perdendo para conectar tudo, algumas frases
# não muita conexão com a ultima e acaba nescessariamente dengligenciando o uso de conectivos.
