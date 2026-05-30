from agno.agent import Agent
from agno.models.openai import OpenAIChat
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("Erro: A variável API_KEY não foi encontrada. Verifique se o arquivo .env está na raiz do projeto.")

agent = Agent(
    model=OpenAIChat(
        id="meta/llama-3.1-8b-instruct",
        api_key=API_KEY,
        base_url="https://integrate.api.nvidia.com/v1"
    ),
    instructions=[
        "Você é um Agente de Boas-Vindas automatizado.",
        "Sua única função é saudar o usuário cordialmente, se apresentar e explicar brevemente que foi criado para demonstrar o poder dos agentes da Agno.",
        "Seja extremamente breve, simpático e responda em no máximo um parágrafo curto."
    ],
    markdown=True
)

print("Agente de Boas-Vindas inicializado. Digite 'sair' para encerrar")

while True:
    entrada = input("Usuário: ")
    if entrada.lower() == "sair":
        print("Encerrando Agente...")
        break
    
    agent.print_response(entrada, stream=True)
    print("\n")