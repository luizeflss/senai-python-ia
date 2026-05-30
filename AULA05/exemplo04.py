from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.db.sqlite import SqliteDb
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("Erro: A variável API_KEY não foi encontrada. Verifique se o arquivo .env está na raiz do projeto.")

agent = Agent(
    model=OpenAIChat(
        id="meta/llama-3.1-8b-instruct",
        api_key=API_KEY,
        base_url="https://integrate.api.nvidia.com/v1"
    ), instructions="""Você é um assistente útil e atencioso que responde de forma didática e clara, sendo muito profissional;
    Responda sempre de forma resumida e educada. Limite sua resposta a no máximo 1 parágrafo.""",
    db=SqliteDb(db_file="agentes.db"),
    add_history_to_context=True,
    num_history_runs= 3,
    markdown=True
)

agent.print_response("Estou trabalhando em um projeto de API em Python", session_id="dev_session")
agent.print_response("Qual framework de teste devo usar ?", session_id="dev_session")
