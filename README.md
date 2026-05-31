<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:c8102e,100:8b0000&height=180&section=header&text=Python%20%2B%20IA&fontSize=68&fontColor=ffffff&fontAlignY=40&desc=SENAI%20•%20Agentes%20e%20Engenharia%20de%20Prompts&descAlignY=62&descSize=17&animation=fadeIn" width="100%"/>

<br/>

[![Python](https://img.shields.io/badge/Python_3.10+-white?style=for-the-badge&logo=python&logoColor=c8102e)](https://python.org)
[![SENAI](https://img.shields.io/badge/SENAI-Curso_IA-c8102e?style=for-the-badge&logoColor=white)](https://www.senai.br)
[![Agno](https://img.shields.io/badge/Agno-AI_Agents-8b0000?style=for-the-badge)](https://github.com/agno-ai/agno)
[![Portfólio](https://img.shields.io/badge/Portfólio-Acadêmico-c8102e?style=for-the-badge)](.)

</div>

---

## 🚀 Senai: Python + Inteligência Artificial

Este repositório foi criado para centralizar, documentar e organizar todas as atividades práticas, relatórios de laboratório e desafios desenvolvidos durante o curso de **Python + Inteligência Artificial** no SENAI.

O objetivo principal deste espaço é registrar a evolução no aprendizado de lógica de programação, manipulação de dados com Python, engenharia de prompts avançada e, na etapa atual, a arquitetura e desenvolvimento de **Agentes Inteligentes Autônomos (AI Agents)** com integração a ferramentas locais e externas (Function Calling).

---

## 📂 Conteúdo do Repositório

O repositório está estruturado para cobrir desde os conceitos manuais de prompt até a automação de sistemas multi-agentes:

- **Laboratórios de Engenharia de Prompts:** Exercícios práticos testando variações de personas, restrições estruturais de tamanho, controle de barreiras de idiomas, cruzamento de contextos complexos e detecção de limites lógicos de LLMs.

- **Desafios Práticos com Frameworks:** Implementações automatizadas em scripts Python utilizando frameworks estruturados do mercado para guiar e extrair a máxima performance dos modelos de linguagem:

<div align="center">

| Framework | Significado |
|:---------:|:------------|
| ![RACE](https://img.shields.io/badge/RACE-c8102e?style=flat-square&logoColor=white) | *Role, Action, Context, Expectation* |
| ![CARE](https://img.shields.io/badge/CARE-a50000?style=flat-square&logoColor=white) | *Context, Action, Result, Example* |
| ![CREATE](https://img.shields.io/badge/CREATE-8b0000?style=flat-square&logoColor=white) | *Character, Request, Engage, Austere, Target, Evaluator* |
| ![CO-STAR](https://img.shields.io/badge/CO--STAR-700000?style=flat-square&logoColor=white) | *Context, Objective, Style, Tone, Audience, Response* |

</div>

- **Desenvolvimento de Agentes Inteligentes (AI Agents):** Scripts práticos empregando o framework *Agno* para criar assistentes autônomos orientados a objetivos com gerenciamento de memória em sessões locais:
  - **Agentes de FAQ de Escopo Fechado:** Chatbots estruturados com guardrails rígidos de contexto para evitar alucinações.
  - **Agentes de Web Scraping:** Automação conectada com `requests` e `BeautifulSoup` para raspagem de artigos, limpeza de tags HTML e sumarização de notícias em tempo real.
  - **Agentes de Análise Financeira (SQL + RAG):** Ingestão automática de dados de ações da bolsa via Yahoo Finance, estruturação de banco de dados relacional com `sqlite3` e consultas inteligentes utilizando ferramentas analíticas paralelas controladas.

---

## 🛠️ Tecnologias e Ferramentas

<div align="center">

| | Tecnologia | Detalhe |
|:---:|:---|:---|
| 🐍 | **Linguagem Principal** | Python 3.10 ou superior |
| 🤖 | **Modelos de IA** | Llama 3.1 8B Instruct (via NVIDIA API Catalog) |
| 📦 | **Orquestração de Agentes** | Framework Agno (antigo Phidata) |
| 💾 | **Armazenamento Local** | SQLite3 (Banco de dados relacional leve em arquivo) |
| 📄 | **Documentação** | Markdown (`.md`) — legível direto no GitHub |

</div>

---

## 📦 Dependências e Bibliotecas Utilizadas

Para garantir a reprodução e execução correta de todos os laboratórios e agentes contidos neste portfólio, as seguintes bibliotecas do ecossistema Python são exigidas:

### 🧠 Core de Inteligência Artificial
- **`agno`**: Framework de orquestração de Agentes autônomos, gerenciamento de conhecimento e integração de ferramentas (*tools*).
- **`openai`**: SDK oficial de conexão com endpoints compatíveis, utilizado para fazer a ponte de comunicação de streaming com a API da NVIDIA.
- **`python-dotenv`**: Gerenciador de variáveis de ambiente de segurança para carregar chaves criptográficas (`API_KEY`) a partir de arquivos `.env` locais, evitando vazamento de credenciais.

### 📊 Coleta, Raspagem e Análise de Dados
- **`yfinance`**: Biblioteca de integração com a API do Yahoo Finance para download de dados históricos de fechamento e volume de ativos de mercado.
- **`pandas`**: Manipulação e análise estruturada de matrizes de dados (DataFrames), essencial na unificação e tratamento de tabelas.
- **`requests`**: Biblioteca cliente HTTP para disparo de requisições e download do código fonte de páginas web.
- **`beautifulsoup4`**: Mecanismo de parsing de estruturas de árvores HTML para extração e limpeza de textos puros (*Web Scraping*).

### 🎙️ Interface Multimídia
- **`gTTS`** (*Google Text-to-Speech*): Biblioteca utilizada para converter os outputs de texto gerados pela Inteligência Artificial em arquivos de áudio locais falados (`.mp3`).

---

## 🚀 Como Executar as Dependências no seu Ambiente

Caso mude de máquina ou clone o portfólio em outro computador, você pode rodar a instalação unificada das bibliotecas utilizando o instalador do Python através do terminal:

```bash
# Se o seu pip global estiver configurado nas variáveis de ambiente:
pip install agno openai python-dotenv yfinance pandas requests beautifulsoup4 gTTS

# Caso utilize um ambiente virtual (.venv) ou precise chamar diretamente o binário do Python:
python -m pip install agno openai python-dotenv yfinance pandas requests beautifulsoup4 gTTS