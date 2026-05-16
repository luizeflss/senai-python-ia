"""
CÓDIGO ORIGINAL
class ProcessadorDeDados:
    def _init_(self, dados):
        self.dados
        dados
    def processar_dados(self):
        if not self.dados or not isinstance(self.dados, list):
            print("Erro: Dados inválidos.")
            return []
        dados_filtrados = []
        for item in self.dados:
            if isinstance(item, int) and item > 0:
                dados_filtrados.append(item)
        dados_transformados = []
        for item in dados_filtrados:
            dados_transformados.append(item*10)
        print(" Relatório de Processamento ---")
        print(f"Total de itens processados: (len(dados_transformados))")
        return dados_transformados
proc = ProcessadorDeDados ([1, 2, 3, 4, "a", 5])
proc.processar_dados ()
"""
#===============================//=================================
#CÓDIGO CORRIGIDO
class ProcessadorDeDados:

    def __init__(self, dados):  # Ajustados os dunders __init__
        self.dados = dados  # Corrigida a atribuição de instância

    def processar_dados(self):
        if not self.dados or not isinstance(self.dados, list):
            print("Erro: Dados inválidos.")
            return []

        dados_filtrados = []
        for item in self.dados:
            if isinstance(item, int) and item > 0:
                dados_filtrados.append(item)

        dados_transformados = []
        for item in dados_filtrados:
            dados_transformados.append(item * 10)

        print("--- Relatório de Processamento ---")
        print(f"Total de itens processados: {len(dados_transformados)}")
        print(f"Dados transformados: {dados_transformados}")
        return dados_transformados


proc = ProcessadorDeDados([1, 2, 3, 4, "a", 5])
proc.processar_dados()

#==============================//=================================
#CÓDIGO REFATORADO
from typing import Any, List


class ProcessadorDeDados:
    """Gerencia pipelines de higienização, transformação e exibição de dados numéricos."""

    def __init__(self, dados_brutos: List[Any]) -> None:
        self._dados = dados_brutos

    def _validar_entrada(self) -> bool:
        """Verifica se a coleção injetada possui conformidade básica estrutural."""
        return isinstance(self._dados, list) and len(self._dados) > 0

    def _filtrar_inteiros_positivos(self) -> List[int]:
        """Extrai apenas valores numéricos inteiros estritamente positivos."""
        return [item for item in self._dados if isinstance(item, int) and item > 0]

    def _aplicar_escala_multiplicadora(self, lista_limpa: List[int]) -> List[int]:
        """Multiplica cada elemento da coleção higienizada pelo fator de escala."""
        return [item * 10 for item in lista_limpa]

    def _emitir_relatorio_metricas(self, dados_finais: List[int]) -> None:
        """Renderiza informações sumárias do processamento final em console."""
        print("\n=== Relatório de Processamento ===")
        print(f"Total de elementos computados: {len(dados_finais)}")
        print(f"Resultado final do lote: {dados_finais}")

    def executar_pipeline(self) -> List[int]:
        """Gerencia a orquestração do fluxo de processamento de dados (Mapeador Único)."""
        if not self._validar_entrada():
            print("Erro Crítico: O dataset fornecido é inválido ou vazio.")
            return []

        dados_filtrados = self._filtrar_inteiros_positivos()
        dados_processados = self._aplicar_escala_multiplicadora(dados_filtrados)

        self._emitir_relatorio_metricas(dados_processados)
        return dados_processados


if __name__ == "__main__":
    dataset_teste = [1, 2, 3, 4, "a", 5]
    processador = ProcessadorDeDados(dataset_teste)
    processador.executar_pipeline()
print("")
