# Exercício 9 — Texto para Fala
# Utilizando gTTS:
# peça um texto usando input()
# transforme em áudio
# salve como fala.mp3
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

palavra = input("Digite o Texto que deseja converter em audio:\n")


# Converter texto em voz
tts = gTTS(
    text=palavra,
    lang="pt"
)

tts.save("ex9.mp3")

print("\nÁudio salvo como ex9.mp3")
