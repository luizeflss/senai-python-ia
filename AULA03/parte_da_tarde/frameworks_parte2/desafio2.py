import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
API_KEY = os.getenv("API_KEY")

# Componentes do Framework CARE
context = "Um estudante da área de tecnologia precisa organizar seu tempo para aprender Git e GitHub."
action = "Monte um plano de estudos focado e prático de 7 dias."
result = "O resultado deve ser um cronograma diário dividindo teoria e prática."
example = "Diretriz: O aluno só tem 45 minutos por dia. Foque apenas nos comandos essenciais (add, commit, push, pull, clone)."

# Montagem do Prompt usando a estrutura CARE
prompt_final = f"""
[CONTEXT]: {context}
[ACTION]: {action}
[RESULT]: {result}
[GUIDELINE]: {example}
"""

cliente = OpenAI(api_key=API_KEY, base_url="https://integrate.api.nvidia.com/v1")

resposta = cliente.chat.completions.create(
    model="meta/llama-3.1-8b-instruct",
    messages=[{"role": "user", "content": prompt_final}],
    temperature=0.5, # Menor temperatura para respostas mais exatas e organizadas
)

print("=================== PROMPT FINAL ENVIADO ===================")
print(prompt_final)
print("===================== RESPOSTA DA I.A ======================")
print(resposta.choices[0].message.content)