from langchain_community.utilities import SQLDatabase
from langchain.tools import tool

db = SQLDatabase.from_uri("sqlite:///Locadora.db")

@tool
def listar_filmes():
    """Listar os filmes cadastrados"""
    return db.run(
        """SELECT titulo FROM Filme"""
    )

print(listar_filmes.invoke({}))

