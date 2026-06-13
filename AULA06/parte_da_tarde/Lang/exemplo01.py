from langchain_community.utilities import SQLDatabase

db = SQLDatabase.from_uri("sqlite:///Locadora.db")
resultado = db.run("""SELECT * FROM Filme""")
print(resultado)