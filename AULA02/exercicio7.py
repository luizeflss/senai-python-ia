"""
CÓDIGO ORIGINAL
def obter_desconto(tipo_cliente, valor_compra):
    if tipo_cliente == "premium":
        if valor_compra > 1000:
            return valor_compra * 0.20
        else:
            return valor_compra * 0.10
    elif tipo_cliente == "gold":
        if valor_compra > 500:
            return valor_compra * 0.15
        else:
            return valor_compra * 0.05
    else:
        return 0
"""
#===============================//=================================
#CÓDIGO CORRIGIDO
def obter_desconto(tipo_cliente, valor_compra):
    if tipo_cliente == "premium":
        if valor_compra > 1000:
            return valor_compra * 0.20
        else:
            return valor_compra * 0.10
    elif tipo_cliente == "gold":
        if valor_compra > 500:
            return valor_compra * 0.15
        else:
            return valor_compra * 0.05
    return 0.0  # Retorno padrão explícito numérico

#==============================//=================================
#CÓDIGO REFATORADO
def calcular_desconto_cliente(tipo_cliente: str, valor_compra: float) -> float:
    """Determina o valor do desconto baseado na categoria do cliente e faixas de preço."""

    # Estrutura de dados mapeando as regras de negócio em formato de tabela limpa
    REGRAS_DESCONTO = {
        "premium": {"limite": 1000, "taxa_alta": 0.20, "taxa_baixa": 0.10},
        "gold": {"limite": 500, "taxa_alta": 0.15, "taxa_baixa": 0.05},
    }

    # Busca o perfil do cliente no dicionário de regras de forma segura
    regragem = REGRAS_DESCONTO.get(tipo_cliente.lower())

    # Caso não seja um tipo elegível cadastrado, o desconto concedido é zero
    if not regragem:
        return 0.0

    # Aplicação direta da regra aritmética sem estruturas if/elif repetitivas
    if valor_compra > regragem["limite"]:
        return valor_compra * regragem["taxa_alta"]

    return valor_compra * regragem["taxa_baixa"]


if __name__ == "__main__":
    print(f"Premium acima de 1000: {calcular_desconto_cliente('premium', 1200)}")
    print(f"Gold na faixa limite: {calcular_desconto_cliente('gold', 600)}")
    print(f"Cliente normal: {calcular_desconto_cliente('normal', 200)}")