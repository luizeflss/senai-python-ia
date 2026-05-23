"""
AULA 03 - Experimento 5: Diferentes Personas

RELATÓRIO:
- Historiador: Destaca o impacto cultural da escrita suméria, tábuas de argila e evolução social.
- Técnico Rabugento: Aborda o tema comparando a escrita antiga a 'protocolos de rede arcaicos', 
  reclamando do tempo de resposta lento do papiro e da falta de backup físico.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
API_KEY = os.getenv("API_KEY")

cliente = OpenAI(api_key=API_KEY, base_url="https://integrate.api.nvidia.com/v1")
modelo_nvidia = "meta/llama-3.1-8b-instruct"

print("====== EXPERIMENTO 5: DIFERENTES PERSONAS ======")

tema_comum = "Escreva um parágrafo sobre a evolução da escrita humana."

# --- PERSONA A: HISTORIADOR ---
persona_historiador = "Você é um historiador acadêmico fascinado pela Idade Média."
print(f"[Enviando para Persona A: Historiador]")
res_persona_a = cliente.chat.completions.create(
    model=modelo_nvidia,
    messages=[
        {"role": "system", "content": persona_historiador},
        {"role": "user", "content": tema_comum}
    ]
)
print(f"\n--- Resposta (Persona Historiador) ---\n{res_persona_a.choices[0].message.content}\n" + "-"*40)

# --- PERSONA B: TÉCNICO DE TI ---
persona_tecnico = "Você é um técnico em informática muito rabugento de 50 anos que odeia papel."
print(f"[Enviando para Persona B: Técnico de TI Rabugento]")
res_persona_b = cliente.chat.completions.create(
    model=modelo_nvidia,
    messages=[
        {"role": "system", "content": persona_tecnico},
        {"role": "user", "content": tema_comum}
    ]
)
print(f"\n--- Resposta (Persona Técnico Rabugento) ---\n{res_persona_b.choices[0].message.content}\n")