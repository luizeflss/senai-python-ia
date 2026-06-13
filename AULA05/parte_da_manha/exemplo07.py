import sqlite3
import pandas as pd

#dataframe
dados={
    "nome":["Du", "Dudu", "Edu"],
    "idade":[7,8,9]
}

df = pd.DataFrame(dados)

print("Dataframe original")
print(df)

#salvar as infromações no sql lite
with sqlite3.connect("escola.db") as conn:
    df.to_sql(
        "alunos",
        conn,
        if_exists="replace",
        index=False
    )

print("\nDados Salvos")

#conexão para leitura dos dados
with sqlite3.connect("escola.db") as conn:
    consulta = pd.read_sql(
        "SELECT * FROM alunos", conn
    )
print("\nDados recuperados do banco!")
print(consulta)