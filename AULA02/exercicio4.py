"""
CÓDIGO ORIGINAL
def processa_dados_a(dados):
    return [x * 2 for x in dados]
def processa_dados_b(dados):
    return [x + 10 for x in dados]
def processa_dados_c(dados):
    return [x - 5 for x in dados]

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = [7, 8, 9]

print(processa_dados_a(lista_a))
print(processa_dados_b(lista_b))
print(processa_dados_c(lista_c))

"""
#===============================//=================================
#CÓDIGO CORRIGIDO
# O código original executa sem erros de interpretador, mantido para espelhamento técnico.
def processa_dados_a(dados):
    return [x * 2 for x in dados]


def processa_dados_b(dados):
    return [x + 10 for x in dados]


def processa_dados_c(dados):
    return [x - 5 for x in dados]


lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = [7, 8, 9]

print(processa_dados_a(lista_a))
print(processa_dados_b(lista_b))
print(processa_dados_c(lista_c))

#==============================//=================================
#CÓDIGO REFATORADO
from typing import Callable, List


def mapear_e_transformar_dados(
    dados: List[int], operacao: Callable[[int], int]
) -> List[int]:
    """Aplica uma função de transformação customizável sobre uma lista de dados."""
    # Centraliza o processamento recebendo a operação dinâmica como argumento
    return [operacao(item) for item in dados]


if __name__ == "__main__":
    lista_a, lista_b, lista_c = [1, 2, 3], [4, 5, 6], [7, 8, 9]

    # Passamos funções anônimas (lambdas) para customizar a regra de negócio instantaneamente
    print(mapear_e_transformar_dados(lista_a, lambda x: x * 2))
    print(mapear_e_transformar_dados(lista_b, lambda x: x + 10))
    print(mapear_e_transformar_dados(lista_c, lambda x: x - 5))