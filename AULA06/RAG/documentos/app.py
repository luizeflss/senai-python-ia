from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceHubEmbeddings
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

embeddings = HuggingFaceHubEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db= FAISS.load_local(
    "base_conhecimento",
    embeddings,
    allow_dangerous_deserialization=True
)

llm = ChatOpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("API_KEY"),
    model="meta/llama-3.1-8b-instruct",
    temperature=0
)

while True:
    pergunta= input("\nPergunta: ")
    if pergunta=="sair":
        break
    documentos=db.similarity_search(
        pergunta,
        k=3
    )
    contexto="\n\n".join(
        doc.page_content
        for doc in documentos
    )
    prompt=f"""
    RESPONDA USANDO O CONTEXTO ABAIXO:
    CONTEXTO:
    {contexto}
    PERGUNTA
    {pergunta}
    """
    resposta = llm.invoke(prompt)
    print("\nResposta:")
    print(resposta.content)
