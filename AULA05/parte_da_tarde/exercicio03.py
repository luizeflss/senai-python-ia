from agno.agent import Agent
from agno.models.openai import OpenAIChat
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

faq_instructions = """
Você é um Chatbot de FAQ (Perguntas Frequentes) especializado na História do Python.
Você só tem autorização para responder às seguintes informações baseadas na sua base de dados oficial:

1. Quem criou o Python?
   - Resposta: O Python foi criado por Guido van Rossum no final dos anos 1980.

2. De onde surgiu o nome "Python"?
   - Resposta: O nome foi inspirado no grupo humorístico britânico 'Monty Python's Flying Circus', do qual Guido era grande fã, e não por causa do réptil.

3. Quando o Python foi lançado oficialmente?
   - Resposta: A primeira versão pública (0.9.0) foi lançada em fevereiro de 1991.

4. Qual é a principal filosofia do Python?
   - Resposta: A legibilidade do código e a simplicidade. Isso está documentado no 'The Zen of Python' (import this).

REGRA CRÍTICA DE CONTROLE DE ESCOPO:
- Se o usuário fizer qualquer pergunta que NÃO esteja diretamente relacionada aos fatos acima (ex: pedir para programar um código, perguntar sobre futebol ou receitas), você DEVE responder exatamente com esta frase ou variação direta: 'Desculpe, eu sou um agente de FAQ restrito e não possuo essa informação na minha base de conhecimentos atual.'
- Nunca invente fatos fora desse escopo.
"""

faq_agent = Agent(
    model=OpenAIChat(
        id="meta/llama-3.1-8b-instruct",
        api_key=API_KEY,
        base_url="https://integrate.api.nvidia.com/v1"
    ),
    instructions=[faq_instructions],
    markdown=True
)

print("Chatbot de FAQ sobre História do Python Ativo. Digite 'sair' para encerrar")

while True:
    entrada = input("Usuário: ")
    if entrada.lower() == "sair":
        print("Encerrando FAQ...")
        break
    
    faq_agent.print_response(entrada, stream=True)
    print("\n")