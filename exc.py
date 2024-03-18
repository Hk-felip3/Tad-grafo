class Grafo:
    def __init__(self, num_vertices):
        # Inicializa o objeto Grafo com o número de vértices especificado
        self.num_vertices = num_vertices
        # Cria uma matriz de adjacência preenchida com zeros
        self.matriz_adj = [[0] * num_vertices for _ in range(num_vertices)]

    def insere_aresta(self, origem, destino):
        # Insere uma aresta na matriz de adjacência entre os vértices de origem e destino
        self.matriz_adj[origem][destino] = 1
        # Se o grafo for não direcionado, descomente a linha abaixo para adicionar a aresta inversa
        # self.matriz_adj[destino][origem] = 1

    def carrega_grafo(self, arquivo):
        # Lê o número de vértices do arquivo e reinicializa o grafo
        num_vertices = int(arquivo.readline().strip())
        self.__init__(num_vertices)

        # Lê a matriz de adjacência do arquivo e a carrega para o grafo
        for i in range(self.num_vertices):
            valores = list(map(int, arquivo.readline().strip().split()))
            for j, valor in enumerate(valores):
                self.matriz_adj[i][j] = valor

    def imprime_grafo(self):
        # Imprime a matriz de adjacência na saída padrão
        print("Matriz de adjacência:")
        for linha in self.matriz_adj:
            print(" ".join(map(str, linha)))


def main():
    # Abre o arquivo contendo a matriz de adjacência do grafo
    with open("grafo.txt", "r") as arquivo:
        # Cria um objeto Grafo
        grafo = Grafo(0)  # Inicializa o grafo com 0 vértices temporariamente
        # Carrega o grafo a partir do arquivo
        grafo.carrega_grafo(arquivo)

    # Imprime o grafo carregado
    grafo.imprime_grafo()


if __name__ == "__main__":
    main()
