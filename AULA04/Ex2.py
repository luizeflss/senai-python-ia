# Exercício 2 — IA Professor
# Altere o system para que a IA:
# aja como um professor de programação
# responda perguntas simples sobre Python
# Teste perguntas como:
# “O que é variável?”
# “O que é loop?”

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

comportamento =input("Digite como você quer que a IA se comporte:\n")
pergunta = input("Digite a sua pergunta para a IA:\n")

resposta = cliente.chat.completions.create(
    model="meta/llama-3.1-8b-instruct",

    messages=[
        {
            "role": "system",
            "content": comportamento
        },

        {
            "role": "user",
            "content": pergunta
        }
    ]
)
print("\nResposta da IA:\n")
print("Ela agira como:"+ comportamento)
print(resposta.choices[0].message.content)

# Resposta:
# Neste codigo eu deixei de maneira mais flexivel para que o usuario possa escolher o comportamento da IA,
# eu achei um resultado bom, ele consgui me responder de maneira clara a minha duvida, acho que a unica coisa
# e que ele não aje da maneira parecida ao gpt, mas acredito que para isso seja apenas uma configuração mais clara.


