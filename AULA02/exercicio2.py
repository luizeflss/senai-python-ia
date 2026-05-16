"""
CÓDIGO ORIGINAL
def soma_pares(lista_numeros):
    total-8
    for numero in lista_numeros
        if numero % 2 != 0:
            total numero
    return total
print(soma_pares([1, 2, 3, 4, 5, 6]))
"""
#===============================//=================================
#CÓDIGO CORRIGIDO
def soma_pares(lista_numeros):
    total = 0  # Inicialização correta da variável
    for numero in lista_numeros:
        if numero % 2 == 0:  # Mudado de != para == para capturar os pares
            total += numero  # Atribuição cumulativa corrigida (+=)
    return total

print(
    soma_pares([1, 2, 3, 4, 5, 6])
)  # Agora retorna corretamente 12 (2 + 4 + 6)

#==============================//=================================
#CÓDIGO REFATORADO
from typing import List

def somar_numeros_pares(numeros: List[int]) -> int:
    """Calcula a soma de todos os números pares em uma lista de forma funcional."""
    # Expressão geradora combinada com a função nativa sum() para máxima eficiência
    return sum(num for num in numeros if num % 2 == 0)

# Teste da função refatorada
if __name__ == "__main__":
    lista_exemplo = [1, 2, 3, 4, 5, 6]
    resultado = somar_numeros_pares(lista_exemplo)
    print(f"Soma dos números pares de {lista_exemplo}: {resultado}")