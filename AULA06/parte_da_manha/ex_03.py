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
# =========================
# 🔧 FERRAMENTA DE SENTIMENTO
# =========================
def analisar_sentimento(texto: str) -> str:
    """Classifica o sentimento de um texto como positivo, negativo ou neutro."""
    palavras_positivas = ["bom", "ótimo", "excelente", "feliz", "incrível", "maravilhoso", "amei", "perfeito", "adorei", "fantástico"]
    palavras_negativas = ["ruim", "péssimo", "horrível", "triste", "odeio", "terrível", "odiei", "detestei", "decepcionante", "horrendo"]

    texto_lower = texto.lower()

    positivas = sum(1 for p in palavras_positivas if p in texto_lower)
    negativas = sum(1 for p in palavras_negativas if p in texto_lower)

    if positivas > negativas:
        sentimento = "POSITIVO"
    elif negativas > positivas:
        sentimento = "NEGATIVO"
    else:
        sentimento = "NEUTRO"

    return f"Sentimento detectado: {sentimento} (palavras positivas: {positivas}, negativas: {negativas})"


# =========================
# 🤖 AGENTE
# =========================
agent = Agent(
    model=OpenAIChat(
        id="meta/llama-3.1-70b-instruct",
        api_key=API_KEY,
        base_url="https://integrate.api.nvidia.com/v1"
    ),
    tools=[analisar_sentimento],
    instructions="""
Você é um agente de análise de sentimento.
Quando receber um texto, SEMPRE use a ferramenta analisar_sentimento antes de responder.
Depois informe o resultado da análise e responda de forma adequada ao sentimento detectado.
""",
    markdown=True
)


# =========================
# 🧠 TEXTOS DE TESTE
# =========================
textos = [
    "Esse produto é incrível, amei cada detalhe!",
    "Que experiência horrível, foi péssimo do início ao fim.",
    "Recebi o pedido hoje.",
]

for texto in textos:
    print(f"\n📝 Texto: {texto}")
    print("-" * 50)
    agent.print_response(texto, stream=True)