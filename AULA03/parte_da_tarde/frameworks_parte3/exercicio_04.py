"""
AULA 03 - Experimento 4: Com vs Sem Definição de Formato (Framework CREATE)

RELATÓRIO:
- Sem Formato: Devolve parágrafos corridos que misturam os conceitos e exigem esforço de leitura.
- Com Formato (CREATE): Renderiza uma tabela Markdown impecável. A leitura visual 
  fica estruturada, dividindo o nome do pilar e o resumo diretamente.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
API_KEY = os.getenv("API_KEY")

cliente = OpenAI(api_key=API_KEY, base_url="https://integrate.api.nvidia.com/v1")
modelo_nvidia = "meta/llama-3.1-8b-instruct"

print("====== EXPERIMENTO 4: COM VS SEM DEFINIÇÃO DE FORMATO (CREATE) ======")

# --- PASSO A: SEM FORMATO ---
prompt_sem_formato = "Quais os pilares do POO?"
print(f"[Enviando Sem Formato]: '{prompt_sem_formato}'")
res_sem_fmt = cliente.chat.completions.create(
    model=modelo_nvidia,
    messages=[{"role": "user", "content": prompt_sem_formato}]
)
print(f"\n--- Resposta Sem Formato ---\n{res_sem_fmt.choices[0].message.content}\n" + "-"*40)

# --- PASSO B: COM FORMATO ---
role_inst = "Você é um instrutor de programação focado em didática visual."
prompt_com_formato = (
    "Liste os 4 pilares do POO. Não use exemplos longos. "
    "Formato de saída obrigatório: Uma tabela Markdown contendo as colunas 'Pilar' e 'Definição Curta'."
)
print(f"[Enviando Com Formato - CREATE]")
res_com_fmt = cliente.chat.completions.create(
    model=modelo_nvidia,
    messages=[
        {"role": "system", "content": role_inst},
        {"role": "user", "content": prompt_com_formato}
    ]
)
print(f"\n--- Resposta Com Formato (CREATE) ---\n{res_com_fmt.choices[0].message.content}\n")