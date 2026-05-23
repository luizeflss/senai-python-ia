import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
API_KEY = os.getenv("API_KEY")

# Componentes do Framework CO-STAR
context = "Uma escola técnica ficou completamente sem sinal de internet e sem dados móveis exatamente 10 minutos antes do início da apresentação dos projetos finais dos alunos do curso de TI."
objective = "Crie 3 soluções de contingência puramente locais e offline para que os alunos consigam projetar e apresentar seus slides e protótipos de sistemas sem depender da nuvem."
style = "Lista de ações em tópicos acionáveis (passo a passo)."
tone = "Pragmático, focado em resolução de problemas e calmo."
audience = "Alunos desesperados e professores avaliadores."
response = "Retorne a resposta estruturada em Markdown, usando negritos para destacar os recursos offline necessários (como roteadores locais, cabos ou pendrives)."

# Montagem do Prompt usando a estrutura CO-STAR
prompt_final = f"""
# CONTEXT
{context}

# OBJECTIVE
{objective}

# STYLE
{style}

# TONE
{tone}

# AUDIENCE
{audience}

# RESPONSE FORMAT
{response}
"""

cliente = OpenAI(api_key=API_KEY, base_url="https://integrate.api.nvidia.com/v1")

resposta = cliente.chat.completions.create(
    model="meta/llama-3.1-8b-instruct",
    messages=[{"role": "user", "content": prompt_final}],
    temperature=0.6,
    max_tokens=450
)

print("=================== PROMPT FINAL ENVIADO ===================")
print(prompt_final)
print("===================== RESPOSTA DA I.A ======================")
print(resposta.choices[0].message.content)