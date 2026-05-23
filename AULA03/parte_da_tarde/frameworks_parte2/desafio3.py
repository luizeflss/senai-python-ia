import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
API_KEY = os.getenv("API_KEY")

# Componentes do Framework CREATE
character = "Você é um Técnico em informática e Professor de arquitetura de computadores."
request = "Explique a diferença entre os principais tipos de memória: RAM, Armazenamento (SSD/HD) e Cache."
engage = "Use uma linguagem didática, clara e objetiva."
austere = "Não escreva parágrafos longos ou textos corridos."
target = "A resposta DEVE estar em formato de tabela Markdown contendo as colunas: | Tipo de Memória | Função Principal | Velocidade Relativa |."
evaluator = "O critério de sucesso é que a tabela seja legível diretamente no GitHub e diferencie claramente a volatilidade de cada uma."

# Montagem do Prompt usando a estrutura CREATE
prompt_final = f"""
- Character: {character}
- Request: {request}
- Tone: {engage}
- Constraints: {austere}
- Output Format: {target}
- Success Criteria: {evaluator}
"""

cliente = OpenAI(api_key=API_KEY, base_url="https://integrate.api.nvidia.com/v1")

resposta = cliente.chat.completions.create(
    model="meta/llama-3.1-8b-instruct",
    messages=[{"role": "user", "content": prompt_final}],
    temperature=0.3, # Baixa temperatura para manter a estrutura da tabela perfeita
    max_tokens=400
)

print("=================== PROMPT FINAL ENVIADO ===================")
print(prompt_final)
print("===================== RESPOSTA DA I.A ======================")
print(resposta.choices[0].message.content)