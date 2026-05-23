"""
AULA 03 - Experimento 2: Linguagem Simples vs Técnica (Framework CARE)

RELATÓRIO:
- Técnica: Foca em herança sob a ótica de escopo, acoplamento e estruturas de classes.
- Simples (CARE): Aborda o tema usando analogias do cotidiano (Veículo e Carro), 
  eliminando jargões intimidantes e focando no reaproveitamento de código.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
API_KEY = os.getenv("API_KEY")

cliente = OpenAI(api_key=API_KEY, base_url="https://integrate.api.nvidia.com/v1")
modelo_nvidia = "meta/llama-3.1-8b-instruct"

print("====== EXPERIMENTO 2: LINGUAGEM SIMPLES VS TÉCNICA (CARE) ======")

# --- PASSO A: LINGUAGEM TÉCNICA ---
prompt_tecnico = "Disserte sobre o mecanismo de herança em Programação Orientada a Objetos."
print(f"[Enviando Prompt Técnico]: '{prompt_tecnico}'")
res_tecnico = cliente.chat.completions.create(
    model=modelo_nvidia,
    messages=[{"role": "user", "content": prompt_tecnico}]
)
print(f"\n--- Resposta Técnica ---\n{res_tecnico.choices[0].message.content}\n" + "-"*40)

# --- PASSO B: LINGUAGEM SIMPLES ---
prompt_simples = (
    "Estou aprendendo POO. Explique o que é herança em programação. "
    "Quero uma explicação de nível iniciante, sem jargões complexos. "
    "Mostre um exemplo prático comparando uma classe 'Veiculo' e uma classe 'Carro'."
)
print(f"[Enviando Prompt Simples - CARE]")
res_simples = cliente.chat.completions.create(
    model=modelo_nvidia,
    messages=[{"role": "user", "content": prompt_simples}]
)
print(f"\n--- Resposta Simples (CARE) ---\n{res_simples.choices[0].message.content}\n")