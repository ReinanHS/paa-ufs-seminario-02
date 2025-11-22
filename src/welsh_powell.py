def welsh_powell(grafo):
    vertices_ordenados = sorted(grafo.keys(), key=lambda v: len(grafo[v]), reverse=True)

    cores_atribuidas = {}

    for vertice in vertices_ordenados:

        cores_vizinhas = set()
        for vizinho in grafo[vertice]:
            if vizinho in cores_atribuidas:
                cores_vizinhas.add(cores_atribuidas[vizinho])

        cor_atual = 0
        while cor_atual in cores_vizinhas:
            cor_atual += 1

        cores_atribuidas[vertice] = cor_atual

    return cores_atribuidas


if __name__ == "__main__":
    meu_grafo = {
        "A": ["B", "C", "D"],
        "B": ["A", "C"],
        "C": ["A", "B", "D", "E"],
        "D": ["A", "C"],
        "E": ["C"],
    }

    resultado = welsh_powell(meu_grafo)

    ordem = sorted(meu_grafo.keys(), key=lambda x: len(meu_grafo[x]), reverse=True)
    print(f"Ordem de processamento (Grau Decrescente): {ordem}")
    print("-" * 30)

    print("Resultado da Coloração:")
    for v in sorted(resultado.keys()):
        print(f"Vértice {v}: Cor {resultado[v]}")
