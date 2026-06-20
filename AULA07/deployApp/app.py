#imports dependencias 
import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings, ChatNVIDIA

#configuração da página do streamlite e api_key
st.set_page_config(
    page_title="FIAT MANUAL",
    page_icon="🪲",
    layout="centered"
    )
st.title("Virtual Assistant Of FIAT PAlIO FIRE MANUAL")
st.write("Como posso ajuda-lo hoje ?")

nvidia_api_key = os.getenv("API_KEY")

if nvidia_api_key:
    try:
        if "API_KEY" in st.secrets:
            nvidia_api_key=st.secrets["API_KEY"]
    except Exception:
        pass
if not nvidia_api_key:
    st.info("Chave API não encontrada, adicione sua chave no arquivo .env ou ao Secrets")
    st.stop()

#carregando RAGs a partir do pdf - criando a vetorização do pdf
@st.cache_resource(show_spinner="Processando o PDF...")
def inicializar_rag():
    nome_arquivo = "material.pdf"

    if not os.path.exists(nome_arquivo):
        st.error(f"Arquivo'{nome_arquivo}' não encontrado")
        st.stop()
    loader = PyPDFLoader(nome_arquivo)
    paginas = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 700,
        chunk_overlap = 200,
    )

    docs=text_splitter.split_documents(paginas)

    embeddings=NVIDIAEmbeddings(
        model="nvidia/nv-embedqa-e5-v5",
        nvidia_api_key=nvidia_api_key,
        model_type="passage"
    )

    vectorstore=FAISS.from_documents(docs, embedding=embeddings)

    return vectorstore.as_retriever(search_kwargs={"k":5})

retrivier=inicializar_rag()

llm=ChatNVIDIA(
    model="meta/llama-3.1-8b-instruct",
    api_key=nvidia_api_key,
    base_url="https://integrate.api.nvidia.com/v1",
    temperature=0.2
)

template_prompt = """
Você é um assistente técnico especializado e prestativo.
Os textos fragmentados de contexto inseridos abaixo foram extraídos de um manual de produtos e serviços que podem estar em outro idioma que não seja o PT-BR.
Mesmo que o material não esteja em PT-BR, você deve obrigatoriamente responder em português brasileiro (PT-BR).

Sua tarefa é analisar o contexto do material e responder às perguntas do usuário de forma clara e direta.
Caso a resposta não possa ser encontrada no contexto fornecido, você deve apontar que ela não existe no manual e que não pode ajudar com essa questão. Não invente informações.

Contexto extraído do PDF:
{context}

Pergunta do usuário: {question}
Resposta (em PT-BR):
"""

prompt=ChatPromptTemplate.from_template(template_prompt)

#pipeline do RAG para evitar alucinações
rag_chain=(
    {"context":retrivier,"question":RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

if "messages" not in st.session_state:
    st.session_state.messages=[{"role":"assistant","content":"Olá! Processei o material com sucesso. O que você deseja saber ?"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt_usuario:=st.chat_input("EX: Qual o significado do código 4?"):
    st.session_state.messages.append({"role":"user","content":prompt_usuario})
    with st.chat_message("user"):
        st.write(prompt_usuario)

    with st.chat_message("assistant"):
        with st.spinner("Consultando o manual técnico..."):
            try:
                resposta=rag_chain.invoke(prompt_usuario)
                st.write(resposta)
                st.session_state.messages.append({"role":"assistant","content":resposta})
            except Exception as e:
                st.error(f"Erro ao processar a requisição da API: {e}")
