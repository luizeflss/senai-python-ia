import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
API_KEY = os.getenv("API_KEY")

# Componentes do Framework RACE
role = "Você é um Chef de cozinha italiano renomado, conhecido por sua abordagem prática e minimalista."
action = "Crie uma receita de macarrão extremamente simples, rápida e barata."
context = "O público-alvo são estudantes universitários que possuem poucos ingredientes na geladeira e pouco tempo."
expectation = "A receita deve ter no máximo 4 passos e focar em sabor utilizando ingredientes comuns do dia a dia."

# Montagem do Prompt usando a estrutura RACE
prompt_final = f"""
[ROLE]: {role}
[ACTION]: {action}
[CONTEXT]: {context}
[EXPECTATION]: {expectation}
"""

cliente = OpenAI(api_key=API_KEY, base_url="https://integrate.api.nvidia.com/v1")

resposta = cliente.chat.completions.create(
    model="meta/llama-3.1-8b-instruct",
    messages=[{"role": "user", "content": prompt_final}],
    temperature=0.7,
)

print("=================== PROMPT FINAL ENVIADO ===================")
print(prompt_final)
print("===================== RESPOSTA DA I.A ======================")
print(resposta.choices[0].message.content)