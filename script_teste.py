import os
from dotenv import load_dotenv

load_dotenv()
chave = os.getenv("API_KEY")
print(f"Chave carregada: {chave}")