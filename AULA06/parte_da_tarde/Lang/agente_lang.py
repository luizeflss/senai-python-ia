import os
from dotenv import load_dotenv
from langchain.tools import tool
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent

load_dotenv()

db=SQLDatabase.from_uri("sqlite:///Locadora.db")

schema = db.get_table_info(
    table_names=[
    "Cliente",
    "Filme",
    "Locacao",
    "ItemLocacao"
    ]
)

@tool
def execute_sql(query: str) -> str:
    """
        Executa consultas SQL
    """
    print("\nSQL:")
    print(query)
    return db.run(query)

llm = ChatOpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("API_KEY"),
    model="meta/llama-3.1-8b-instruct",
    temperature=0
)

SYSTEM_PROMPT= f"""
Voce é um especialista em linguagem SQL e Banco de Dados.
Banco dísponivel : {schema}

Regras:
 - Utilize execute_sql
 - Use apenas SELECT
 - Responda no idioma pt-br
 - Mostre os dados retornados pela consulta
 - Não escreva apenas o formato do resultado
 - Sempre apresente os valores encontrados
 - Por fim, explique os resultados encontrados de forma simples e em pt-br
"""

agent = create_agent(
    model= llm,
    tools= [execute_sql],
    system_prompt= SYSTEM_PROMPT
)

while True:
    pergunta= input("\nPergunta: ")
    if pergunta.lower()=="sair":
        break
    resposta= agent.invoke(
        {
            "messages":[{
                "role":"user",
                "content":pergunta
            }]
        }
    )
    print("\nRespostas")
    print(resposta["messages"][-1].content)
