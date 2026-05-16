"""
CÓDIGO ORIGINAL

def saudacao (nome)
print("Olá, " + nome + "!")
saudacao ("Mundo")
"""
#===============================//=================================
#CÓDIGO CORRIGIDO
def saudacao(nome):  # Adicionado o ':'
    print("Olá, " + nome + "!")  # Adicionada a indentação correta

saudacao("Mundo")

#==============================//=================================
#CÓDIGO REFATORADO
def saudar_usuario(nome: str) -> None:
    """Exibe uma mensagem de boas-vindas ao usuário usando f-string."""
    # Usamos f-strings para uma interpolação de strings mais limpa e moderna
    print(f"Olá, {nome}!")

# Execução do método principal
if __name__ == "__main__":
    saudar_usuario("Mundo")
print("")