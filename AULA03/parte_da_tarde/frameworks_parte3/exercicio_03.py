"""
AULA 03 - Experimento 3: Com vs Sem Contexto

RELATÓRIO:
- Sem Contexto: Fornece clichês de produtividade universais e abstratos.
- Com Contexto: Fornece planos de estudos fragmentados adaptados para quem tem a 
  mente cansada pós-trabalho, gerando técnicas práticas como a micro-pomodoro.
"""

from openai import OpenAI
import time
from API import API

cliente = OpenAI(api_key=API, base_url="https://integrate.api.nvidia.com/v1")
modelo_nvidia = "meta/llama-3.1-8b-instruct"

print("====== EXPERIMENTO 3: COM VS SEM CONTEXTO ======")

# --- PASSO A: SEM CONTEXTO ---
prompt_sem_contexto = "Como otimizar o tempo?"
print(f"[Enviando Sem Contexto]: '{prompt_sem_contexto}'")
res_sem_ctx = cliente.chat.completions.create(
    model=modelo_nvidia,
    messages=[{"role": "user", "content": prompt_sem_contexto}]
)
print(f"\n--- Resposta Sem Contexto ---\n{res_sem_ctx.choices[0].message.content}\n" + "-"*40)

time.sleep(5)

# --- PASSO B: COM CONTEXTO ---
prompt_com_contexto = (
    "Contexto: Sou estudante de programação, trabalho 8h por dia e só tenho as noites livres. "
    "Crie 3 estratégias de gerenciamento de tempo focadas em evitar a procrastinação nos estudos de Python."
)
print(f"[Enviando Com Contexto]")
res_com_ctx = cliente.chat.completions.create(
    model=modelo_nvidia,
    messages=[{"role": "user", "content": prompt_com_contexto}]
)
print(f"\n--- Resposta Com Contexto ---\n{res_com_ctx.choices[0].message.content}\n")