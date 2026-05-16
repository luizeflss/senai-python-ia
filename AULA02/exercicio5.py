"""
CÓDIGO ORIGINAL
def processar_pedido(status, quantidade, estoque):
    if status == "aprovado":
        if quantidade > 0:
            if estoque >= quantidade:
                return "Pedido processado com sucesso!"
            else:
                return "Erro: Estoque insuficiente."
        else:
            return "Erro: Quantidade inválida."
    else:
        return "Erro: Status do pedido não aprovado."
"""
#===============================//=================================
#CÓDIGO CORRIGIDO
# O código original funciona logicamente, mas sua legibilidade está severamente comprometida.
def processar_pedido(status, quantidade, estoque):
    if status == "aprovado":
        if quantidade > 0:
            if estoque >= quantidade:
                return "Pedido processado com sucesso!"
            else:
                return "Erro: Estoque insuficiente."
        else:
            return "Erro: Quantidade inválida."
    else:
        return "Erro: Status do pedido não aprovado."

#==============================//=================================
#CÓDIGO REFATORADO
def processar_pedido_seguro(status: str, quantidade: int, estoque: int) -> str:
    """Avalia o status de um pedido de vendas usando cláusulas de guarda para validação precoce."""

    # Cláusulas de guarda interceptam os cenários de erro logo no início da função
    if status != "aprovado":
        return "Erro: Status do pedido não aprovado."

    if quantidade <= 0:
        return "Erro: Quantidade inválida."

    if estoque < quantidade:
        return "Erro: Estoque insuficiente."

    # Caminho feliz (Happy Path) fica limpo ao final, sem aninhamento desnecessário
    return "Pedido processado com sucesso!"


if __name__ == "__main__":
    print(processar_pedido_seguro("aprovado", 5, 10))
    print(processar_pedido_seguro("aprovado", 5, 3))
    print(processar_pedido_seguro("pendente", 5, 10))