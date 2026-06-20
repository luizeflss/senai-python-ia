import os
from dotenv import load_dotenv

load_dotenv()
chaveNVIDIA = os.getenv("API_KEY")
chaveHUGGINGFACE = os.getenv("HUGGINGFACEHUB_API_TOKEN")
print(f"Chave carregada: {chaveNVIDIA}")
print(f"Chave carregada: {chaveHUGGINGFACE}")