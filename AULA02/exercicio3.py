"""
CÓDIGO ORIGINAL
def filtra_e_dobra(numeros):
    resultado = []
    for num in numeros:
        if num > 5:
            resultado.append(num * 2)
    return resultado
print(filtra_e_dobra([1, 6, 3, 8, 2, 10]))
"""
#===============================//=================================
#CÓDIGO CORRIGIDO
def filtra_e_dobra(numeros):
    resultado = []
    for num in numeros:
        if num > 5:
            resultado.append(num * 2)
    return resultado

print(filtra_e_dobra([1, 6, 3, 8, 2, 10]))

#==============================//=================================
#CÓDIGO REFATORADO
from typing import List

def filtrar_e_dobrar_valores(numeros: List[int]) -> List[int]:
    """Filtra números maiores que 5 e retorna seus valores multiplicados por 2."""
    #Sintaxe compacta e idiomática usando List Comprehension
    return [num * 2 for num in numeros if num > 5]

if __name__ == "__main__":
    dados_entrada = [1, 6, 3, 8, 2, 10]
    print(f"Resultado processado: {filtrar_e_dobrar_valores(dados_entrada)}")