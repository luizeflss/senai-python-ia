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

resposta = cliente.chat.completions.create(
    model="meta/llama-3.1-8b-instruct",
    messages=[
        {
            "role": "user",
            "content": "Escreva uma história curta sobre o alucard"
        }
    ]
)

print(resposta.choices[0].message.content)