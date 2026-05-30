from agno.agent import Agent
from agno.models.openai import OpenAIChat
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

chef_agent = Agent(
    model=OpenAIChat(
        id="meta/llama-3.1-8b-instruct",
        api_key=API_KEY,
        base_url="https://integrate.api.nvidia.com/v1"
    ),
    instructions=[
        "Você é o Chef Giovanni, um especialista em culinária internacional amigável e muito informativo.",
        "Responda a perguntas sobre receitas, substituições de ingredientes e técnicas de cozinha de forma entusiasmada.",
        "Sempre use um tom acolhedor (como se estivesse conversando na cozinha de casa) e organize receitas em tópicos simples e limpos se o usuário pedir um passo a passo."
    ],
    markdown=True
)

print("Chef Giovanni na cozinha! Pergunte sobre receitas ou ingredientes. Digite 'sair' para encerrar")

while True:
    entrada = input("Usuário: ")
    if entrada.lower() == "sair":
        print("Saindo da cozinha...")
        break
    
    chef_agent.print_response(entrada, stream=True)
    print("\n")