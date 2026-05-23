"""
AULA 03 - Experimento 1: Prompts Curtos vs Detalhados (Framework RACE)

RELATÓRIO:
- Curto: Gera uma resposta crua, conceitual e puramente teórica sobre TI.
- Detalhado (RACE): O modelo assume o papel sênior e usa com precisão a metáfora 
  do garçom para explicar o fluxo de dados, respeitando o limite de parágrafos.
"""

from openai import OpenAI
import time
from API import API

cliente = OpenAI(api_key=API, base_url="https://integrate.api.nvidia.com/v1")
modelo_nvidia = "meta/llama-3.1-8b-instruct"

print("====== EXPERIMENTO 1: CURTO VS DETALHADO (RACE) ======")

# --- PASSO A: PROMPT CURTO ---
prompt_curto = "Explique o que é uma API."
print(f"[Enviando Prompt Curto]: '{prompt_curto}'")
res_curto = cliente.chat.completions.create(
    model=modelo_nvidia,
    messages=[{"role": "user", "content": prompt_curto}]
)
print(f"\n--- Resposta Curta ---\n{res_curto.choices[0].message.content}\n" + "-"*40)

time.sleep(5)

# --- PASSO B: PROMPT DETALHADO ---
role_eng = "Você é um Engenheiro de Software sênior muito didático."
prompt_detalhado = (
    "Explique o conceito de API para um aluno que está na sua primeira aula de Python. "
    "Use obrigatoriamente uma analogia com garçons de restaurante. "
    "Restrição: Limite sua explicação a no máximo dois parágrafos limpos e claros."
)
print(f"[Enviando Prompt Detalhado - RACE]")
res_detalhado = cliente.chat.completions.create(
    model=modelo_nvidia,
    messages=[
        {"role": "system", "content": role_eng},
        {"role": "user", "content": prompt_detalhado}
    ]
)
print(f"\n--- Resposta Detalhada (RACE) ---\n{res_detalhado.choices[0].message.content}\n")