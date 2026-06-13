import pyautogui
import time
import pyperclip
from pathlib import Path

from agno.agent import Agent
from agno.models.openai import OpenAIChat
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("Erro: A variável API_KEY não foi encontrada. Verifique se o arquivo .env está na raiz do projeto.")

#elemento de segurança básica
pyautogui.PAUSE = 0.5

def clicar(x:int,y:int) -> str:
        pyautogui.click(x,y)
        return f"Cick em {x} e {y}"

def escrever(texto:str) -> str:
      pyautogui.write(texto,interval=0.05)
      return f"Escrivi: {texto}"

def abrir_notas() -> str:
      pyautogui.press("win")
      time.sleep(0.5)
      pyautogui.write("Bloco de Notas")
      time.sleep(0.5)
      pyautogui.press("enter")
      time.sleep(1.5)
      return f"Bloco De Notas aberto!"

def print_tela() -> str:
    nome_arquivo = "tela.png"
    pyautogui.screenshot(nome_arquivo)
    # CORREÇÃO: Descobre o caminho completo exato de onde o arquivo foi salvo no seu PC
    caminho_completo = os.path.abspath(nome_arquivo)
    return f"A captura de tela foi salva com sucesso no caminho físico: {caminho_completo}"

jarvis = Agent(
    model=OpenAIChat(
        id="meta/llama-3.1-8b-instruct",
        api_key=API_KEY,
        base_url="https://integrate.api.nvidia.com/v1"
    ),
    markdown=True,
    instructions=[
        "Você é um assistente virtual no estilo J.A.R.V.I.S.",
        "Você controla o computador utilizando ferramentas locais de automação.",
        "REGRAS CRÍTICAS DE EXECUÇÃO:",
        "1. Você DEVE usar APENAS UMA ferramenta por vez. NUNCA chame múltiplas ferramentas simultaneamente.",
        "2. Chame a primeira ferramenta, aguarde o retorno, depois chame a segunda ferramenta, e assim por diante.",
        "3. Ao finalizar, você deve obrigatoriamente relatar ao usuário onde o print foi salvo utilizando a resposta da ferramenta."
    ],
    tools=[
        clicar, escrever, abrir_notas, print_tela
    ]
)

jarvis.print_response(
    """
    Siga estes passos um de cada vez:
    Passo 1: Abra o Bloco de Notas.
    Passo 2: Escreva exatamente: Olá, eu sou um Assistente Virtual criado durante o curso de Inteligência Artificial do SENAI.
    Passo 3: Tire um print da tela e me confirme o local exato onde o arquivo foi salvo.
    """,
    stream=True
)