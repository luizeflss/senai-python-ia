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
    "Você é um tradutor de texto muito experiente"
)

idioma = "francês"

texto_base = (
    "O Exterminador do Futuro gira em torno de"
    "uma guerra nuclear apocalíptica deflagrada"
    "por uma Inteligência Artificial chamada Skynet."
    "Para vencer a humanidade, as máquinas usam viagens no tempo para alterar"
    "a história, enviando ciborgues assassinos ao passado para eliminar os"
    "líderes da resistência"
)

print(f"\nPreparando a tradução do texto no idioma: {idioma}")
print(f"Texto base: {texto_base}\n")

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
                f"Traduza o texto base para "
                f"{texto_base} "
                f"para o idioma {idioma}."
            )
        }
    ]
)

print("--- Resposta da IA ---")
print(resposta.choices[0].message.content)
print("---------------------\n")