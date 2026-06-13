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

if not API_KEY:
    raise ValueError("Erro: A variável API_KEY não foi encontrada. Verifique se o arquivo .env está na raiz do projeto.")

def extrair_texto(url:str)->str:
    headers={
        "User-Agent":"Mozzila/5.0" 
    }

    response= requests.get(url,headers=headers)
    response.raise_for_status()

    soup=BeautifulSoup(response.text, "html.parser")

    for tag in soup(["script","Style","noscript"]):tag.decompose()

    texto = soup.get_text(separator=" ",strip=True)

    return texto[:2000]

url="https://g1.globo.com/sp/sorocaba-jundiai/noticia/2026/05/29/sorocaba-e-jundiai-ampliam-vacinacao-contra-a-gripe.ghtml"

conteudo=extrair_texto(url)
agent = Agent(
    model=OpenAIChat(
        id="meta/llama-3.1-8b-instruct",
        api_key=API_KEY,
        base_url="https://integrate.api.nvidia.com/v1"
    ),
    markdown=True
)

agent.print_response(
    f"""Analise o conteúdo abaixo extraído da página {conteudo}
    Sua tarefas são:
    -Diga qual é o tema principal
    -Liste as informações mais importantes
    -Resuma o conteúdo em 3 frases""")