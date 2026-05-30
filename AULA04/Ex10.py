# Exercício 10 — IA + Voz
# Junte:
# NVIDIA API
# gTTS
# O programa deve:
# enviar pergunta para IA
# receber resposta
# transformar resposta em voz
# salvar áudio

from gtts import gTTS
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

palavra = input("Qual a sua duvida de hoje?\n")

# Gera resposta da IA
resposta = cliente.chat.completions.create(
    model="meta/llama-3.1-8b-instruct",

    messages=[
        {
            "role": "system",
            "content": "Seja fiel ao texto para ser narrado em voz alta"
        },

        {
            "role": "user",
            "content": palavra
        }
    ]
)

texto = resposta.choices[0].message.content

print("\nResposta:\n")
print(texto)
# Converter texto em voz
tts = gTTS(
    text=texto,
    lang="pt"
)

tts.save("ex10.mp3")

print("\nÁudio salvo como ex10.mp3")