from pathlib import Path
import sqlite3
import pandas as pd
import yfinance as yf

from agno.tools.pandas import PandasTools
from agno.tools.sql import SQLTools
from agno.tools.yfinance import YFinanceTools
from agno.agent import Agent
from agno.models.openai import OpenAIChat

import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("Erro: A variável API_KEY não foi encontrada. Verifique se o arquivo .env está na raiz do projeto.")

DB_PATH = Path(__file__).with_name("market_data.db")

def preparar_banco():
    tickers=["NVDA", "AAPL", "MSFT"]
    linhas=[]

    for ticker in tickers:
        historico=yf.Ticker(ticker).history(
            period="5d",
            interval="1d"
        )
        if historico.empty:
            continue
        historico = historico.reset_index()

        if "Date" in historico.columns:
            historico=historico.rename(columns={"Date":"data"})
        elif "Datetime" in historico.columns:
            historico=historico.rename(columns={"Datetime":"data"})

        historico["Ticker"]=ticker

        historico = historico.rename(
            columns={
                "Close":"fechamento",
                "Volume":"volume"
            }
        )

        historico = historico[["data", "Ticker", "fechamento", "volume"]]

        linhas.append(historico)

        if linhas:
            df_historico = pd.concat(linhas,ignore_index=True)
        else:
            df_historico = pd.DataFrame(
                [{
                    "data":pd.Timestamp.utcnow().normalize(),
                    "Ticker":"NVIDIA",
                    "fechamento":0.0,
                    "volume":0
                }]
            )
        with sqlite3.connect(DB_PATH) as conn:
            df_historico.to_sql(
                "historico_precos",
                conn,
                if_exists="replace",
                index=False
            )

preparar_banco()

agent = Agent(
    model=OpenAIChat(
        id="meta/llama-3.1-8b-instruct",
        api_key=API_KEY,
        base_url="https://integrate.api.nvidia.com/v1"
    ),
    tools=[
        YFinanceTools(
            enable_stock_price=True,
            enable_analyst_recommendations=True,
            enable_stock_fundamentals=True
        ),
        PandasTools(),
        SQLTools(
            db_url=f"sqlite:///{DB_PATH.as_posix()}"
        )
    ],
    description=[
        "Você é um analista de investimentos com mais de 10 anos de experiência",
        "Você utiliza dados em SQL e análise de mercado para responder"
    ],
    instructions=[
        "Use markdowns em todas as suas respostas",
        "Utilize tabelas sempre que possível",
        "Consulte SQL para dados locais(historico_precos)",
        "REGRAS DE FERRAMENTAS: Você DEVE usar UMA ferramenta por vez.",
        "NUNCA chame múltiplas ferramentas simultaneamente. Execute uma, espere o resultado, e só depois chame outra."
    ],
    markdown=True
)

agent.print_response(
    """
    Passo 1: Utilize a biblioteca YFinance para obter o preço e recomendações da AAPL (Apple).
    Passo 2: Depois consulte o banco de dados SQLite(historico_precos) para ver os dados recentes.
    """,
    stream=True
)
