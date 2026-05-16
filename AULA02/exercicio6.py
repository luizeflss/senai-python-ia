"""
CÓDIGO ORIGINAL
def ler_arquivo_manual(nome_arquivo):
    f = open(nome_arquivo, "r")
    conteudo = f.read()
    f.close()
    return conteudo
"""
#=================================================================

#CÓDIGO CORRIGIDO
def ler_arquivo_manual(nome_arquivo):
    f = open(nome_arquivo, "r")
    try:
        conteudo = f.read()
        return conteudo
    finally:
        f.close()  # Garante o fechamento mesmo ocorrendo erros internos

#=================================================================

#CÓDIGO REFATORADO
def ler_conteudo_arquivo(caminho_arquivo: str) -> str:
    """Lê o conteúdo de um arquivo de texto de forma segura usando Gerenciador de Contexto."""

    # O operador 'with' gerencia automaticamente a alocação e desalocação do recurso
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        return arquivo.read()


if __name__ == "__main__":
    # Escrita inicial de teste externa
    with open("teste.txt", "w", encoding="utf-8") as f:
        f.write("Olá, mundo!")

    print(ler_conteudo_arquivo("teste.txt"))