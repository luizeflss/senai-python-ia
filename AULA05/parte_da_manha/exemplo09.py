from agno.agent import Agent
from agno.models.openai import OpenAIChat
import os
from dotenv import load_dotenv
from agno.tools.yfinance import YFinanceTools

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
    tools=[YFinanceTools(
        enable_stock_price=True
    )],
    markdown=True
)

agent.print_response(
    "Qual é o preço atual das ações na Apple ?",
    stream=True
    )