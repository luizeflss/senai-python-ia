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

PERFIL_FILE = "perfil.json"

def carregar_perfil():
    if os.path.exists(PERFIL_FILE):
        with open(PERFIL_FILE) as f:
            return json.load(f)
    return {}

def salvar_nome(nome: str) -> str:
    """Salva o nome do usuário no perfil persistente."""
    perfil = carregar_perfil()
    perfil["nome"] = nome
    with open(PERFIL_FILE, "w") as f:
        json.dump(perfil, f)
    return f"Nome '{nome}' salvo com sucesso."

def salvar_comida_favorita(comida: str) -> str:
    """Salva a comida favorita do usuário no perfil persistente."""
    perfil = carregar_perfil()
    perfil["comida"] = comida
    with open(PERFIL_FILE, "w") as f:
        json.dump(perfil, f)
    return f"Comida favorita '{comida}' salva com sucesso."

# Monta contexto com o que já existe no perfil
perfil = carregar_perfil()
if perfil:
    contexto = f"""Você já conhece este usuário: nome='{perfil.get('nome', '?')}', comida favorita='{perfil.get('comida', '?')}'.
Cumprimente-o pelo nome logo no início. Se ainda faltar alguma informação, pergunte."""
else:
    contexto = """Você não conhece o usuário ainda.
Pergunte o nome e a comida favorita. Assim que o usuário informar, use as ferramentas salvar_nome e salvar_comida_favorita imediatamente para guardar."""

print("🤖 Chatbot com perfil persistente (digite 'sair' para encerrar)\n")

API_KEY = os.getenv("API_KEY")
agent = Agent(
    model=OpenAIChat(
        id="meta/llama-3.1-8b-instruct",
        api_key=API_KEY,
        base_url="https://integrate.api.nvidia.com/v1",
        instructions=contexto
    ),
    markdown=True
)

while True:
    entrada = input("Você: ").strip()
    if entrada.lower() == "sair":
        break
    agent.print_response(entrada, stream=True)
    print()