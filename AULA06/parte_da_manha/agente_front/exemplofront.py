import streamlit as st
import os

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv
from agno.db.sqlite import SqliteDb

load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("Erro: A variável API_KEY não foi encontrada. Verifique se o arquivo .env está na raiz do projeto.")


st.set_page_config(
    page_title="Agente de I.A com memória",
    page_icon="👽",
    layout="wide"
)
st.title="FRONT-END I.A SENAI"
st.markdown("Conversa com um agente agente inteligente que mantém histórico de iteração")

if "agente" not in st.session_state:
    st.session_state.agente=Agent(
        model=OpenAIChat(
            id="meta/llama-3.1-8b-instruct",
            api_key=API_KEY,
            base_url="https://integrate.api.nvidia.com/v1"
        ),
        markdown=True,
        instructions=[
            "Você é um assistente útil e profissional."
            "Responda de forma clara, pedagógica e resumida.",
            ],
            db=SqliteDb(db_file="agente.db"),
            add_history_to_context=True,
            num_history_runs=3
    )   

if "messages" not in st.session_state:
    st.session_state.messages=[]

st.subheader("Histórico da conversa")
chat_container=st.container()

with chat_container:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):st.markdown(message["content"])

user_input = st.chat_input("Digite a sua mesagem aqui: ")

if user_input:
    st.session_state.messages.append({
        "role":"user",
        "content":user_input
    })
    with chat_container:
        with st.chat_message("user"):
            st.markdown(user_input)

    with st.spinner("Agente pensando..."):
        try:
            response=st.session_state.agente.run(
                user_input,
                session_id="sessão_1"
            )
            response_text=(
                response.content
                if hasattr(response,'content')
                else str(response)
            )
            st.session_state.messages.append({
                "role":"user",
                "content":response_text
            })
            with chat_container:
                with st.chat_message("assistant"):st.markdown(response_text)
        except Exception as e:
            st.error(f"Erro ao processar a solicitação: {e}")

with st.sidebar:
    st.title="Configurações"
    if st.button("Limpar Conversa"):
        st.session_state.messages=[]
        st.rerun()
    st.divider()
    st.subheader("Informações")
    st.info(
        """
        **MODELO:** llama-3.1-8b-instruct (NVIDIA)
        **BANCO:** SQlite
        **MEMORIA:** Ultimas 3 interações
        **AUTOR:** Luiz Eduardo
    """
    )
    st.divider()
    st.caption(f"total de menssagens:{len(st.session_state.messages)}")