#imports openai
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.db.sqlite import SqliteDb

#imports api_key
import os
from dotenv import load_dotenv
from openai import OpenAI

#imports exercicio
import requests
from bs4 import BeautifulSoup

load_dotenv()

API_KEY = os.getenv("API_KEY")
agent = Agent(
    model=OpenAIChat(
        id="meta/llama-3.1-8b-instruct",
        api_key=API_KEY,
        base_url="https://integrate.api.nvidia.com/v1"
    ),
    markdown=True
)

# Preço em libras (£) — site usa essa moeda
PRECO_ALVO = 50.00

# Livro de exemplo no site de treino para scraping
URL = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

HEADERS = {"User-Agent": "Mozilla/5.0"}


def extrair_preco(url: str) -> float | None:
    response = requests.get(url, headers=HEADERS, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    tag = soup.find("p", class_="price_color")
    if not tag:
        return None

    # Remove símbolo £ e converte para float
    texto = tag.get_text(strip=True).replace("£", "").replace("Â", "").strip()
    return float(texto)


def monitorar(intervalo_segundos: int = 10):
    print(f"🔍 Monitorando produto...")
    print(f"🎯 Preço alvo: £{PRECO_ALVO:.2f}")
    print(f"🔗 URL: {URL}\n")

    while True:
        try:
            preco = extrair_preco(URL)

            if preco is None:
                print("⚠️  Preço não encontrado.")
            else:
                print(f"💰 Preço atual: £{preco:.2f}")

                if preco < PRECO_ALVO:
                    print(f"🚨 ALERTA! Preço abaixo do alvo!")
                    print(f"   £{preco:.2f} < £{PRECO_ALVO:.2f} — HORA DE COMPRAR!")
                else:
                    print(f"   Ainda acima do alvo. Aguardando...")

        except Exception as e:
            print(f"❌ Erro: {e}")

        print(f"⏱️  Próxima verificação em {intervalo_segundos}s...\n")
        time.sleep(intervalo_segundos)


monitorar(intervalo_segundos=10)