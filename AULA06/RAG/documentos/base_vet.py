from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceHubEmbeddings
from langchain_community.document_loaders import PyPDFLoader

arquivos = [
    "AULA06/RAG/documentos/Regimento_SENAI.pdf",
    "AULA06/RAG/documentos/plano_de_curso_ai.pdf"
]

docs=[]

for arquivo in arquivos:
    loader = PyPDFLoader(arquivo)
    docs.extend(loader.load())

splitter = RecursiveCharacterTextSplitter(
    chunk_size= 1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(docs)

embeddings = HuggingFaceHubEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = FAISS.from_document(
    chunks,
    embeddings
)

vectorstore.save_local("base_conhecimento")