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

# --- Parâmetros que os alunos irão modificar ---
personalidade = (
    "Você é samurai sábio."
)

idioma = "português do Brasil(pt-br)"

tamanho_resposta = (
    "com no máximo 15 palavras" \
    "em uma única frase"
)

tema_historia = (
    "um samurai com anos de sabedoria da era taisho do japão"
)

print(f"\nPreparando a história com a personalidade: {personalidade}")
print(f"No idioma: {idioma}")
print(f"Sobre o tema: {tema_historia}\n")

resposta = cliente.chat.completions.create(
    model="meta/llama-3.1-8b-instruct",  # Modelo da NVIDIA

    messages=[
        {
            "role": "system",
            "content": (
                f"{personalidade} "
                f"Responda em {idioma}."
            )
        },

        {
            "role": "user",
            "content": (
                f"Escreva uma história de ninar "
                f"{tamanho_resposta} "
                f"sobre {tema_historia}."
            )
        }
    ]
)

print("--- Resposta da IA ---")
print(resposta.choices[0].message.content)
print("---------------------\n")