import sys
import itertools

INF = 99999
ORDEMMG = 16


class Aresta:
    def __init__(self, nome, distancia):
        self.nome = nome
        self.distancia = distancia


class Vertice:
    def __init__(self, nome):
        self.nome = nome
        self.arestas = []


def acrescenta_aresta(G, v1, v2, distancia):
    G[v1].arestas.append(Aresta(v2, distancia))
    if v1 != v2:
        G[v2].arestas.append(Aresta(v1, distancia))


def get_distancia(G, start, end):
    for a in G[start].arestas:
        if a.nome == end:
            return a.distancia
    return INF


# Variáveis globais
dist_total = []
dist_cada = []
sequencia_locais = []

path = [[-1]*ORDEMMG for _ in range(ORDEMMG)]


def floyd_warshall(G, ordemG, conjunto_locais, inicio):
    dist = [[INF]*ordemG for _ in range(ordemG)]

    for i in range(1, ordemG):
        for j in range(1, ordemG):
            if i == j:
                dist[i][j] = 0
                path[i][j] = 0
            elif get_distancia(G, i, j) != INF:
                dist[i][j] = get_distancia(G, i, j)
                path[i][j] = i
            else:
                dist[i][j] = INF
                path[i][j] = -1

    for k in range(1, ordemG):
        for i in range(1, ordemG):
            for j in range(1, ordemG):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    path[i][j] = path[k][j]

    calcula_permutacoes(conjunto_locais, inicio, dist)

    print_floyd_warshall(dist)
    print_path_array()

# cálculo de distâncias


def calcula_permutacoes(locais, inicio, dist):
    global dist_total, dist_cada, sequencia_locais

    for perm in itertools.permutations(locais):
        dist_total_aux = 0
        dist_cada_aux = []

        dist_total_aux += dist[inicio][perm[0]]
        dist_cada_aux.append(dist[inicio][perm[0]])

        for i in range(len(perm)-1):
            d = dist[perm[i]][perm[i+1]]
            dist_total_aux += d
            dist_cada_aux.append(d)

        if not dist_total or dist_total_aux < dist_total[0]:
            dist_total = [dist_total_aux]
            dist_cada = dist_cada_aux
            sequencia_locais = list(perm)

# Para impressão


def print_floyd_warshall(dist):
    print("Matriz de menor distância entre todos os pares:")
    for i in range(1, ORDEMMG):
        for j in range(1, ORDEMMG):
            print(f"{dist[i][j] if dist[i][j] != INF else 'INF':>5}", end=" ")
        print()
    print()


def print_path_array():
    print("Matriz de caminhos:")
    for i in range(1, ORDEMMG):
        for j in range(1, ORDEMMG):
            print(f"{path[i][j]:>5}", end=" ")
        print()
    print()


def reconstruir_caminho(v, u):
    if path[v][u] == -1:
        return []
    caminho = [u]
    while u != v:
        u = path[v][u]
        if u == 0:
            break
        caminho.append(u)
    return caminho[::-1]


def print_resultados(inicio):
    print(
        f"\nResultado final para o caminho mais curto iniciando no vértice {inicio}")
    print(f"Conjunto de waypoints: {sequencia_locais}")
    print(f"Sequência de waypoints para passeio mais curto: [{inicio}, " + ", ".join(
        map(str, sequencia_locais)) + "]")
    print("Distância de cada trecho:")
    print(f"{inicio} -> {sequencia_locais[0]} = {dist_cada[0]}")
    for i in range(len(sequencia_locais)-1):
        print(
            f"{sequencia_locais[i]} -> {sequencia_locais[i+1]} = {dist_cada[i+1]}")
    print(f"Distância total: {dist_total[0]}")

    # exibe o menor caminho completo reconstruído ---
    print("Menor caminho:")
    caminho_completo = [inicio]
    atual = inicio
    for prox in sequencia_locais:
        trecho = reconstruir_caminho(atual, prox)
        if trecho and trecho[0] == atual:
            trecho = trecho[1:]  # evita repetição
        caminho_completo += trecho
        atual = prox
    print(" -> ".join(map(str, caminho_completo)))
    print()


# Criando o grafo
G = [Vertice(i) for i in range(ORDEMMG)]

# Adicionando arestas
acrescenta_aresta(G, 1, 2, 50)
acrescenta_aresta(G, 1, 3, 40)
acrescenta_aresta(G, 1, 4, 10)
acrescenta_aresta(G, 2, 7, 60)
acrescenta_aresta(G, 3, 5, 20)
acrescenta_aresta(G, 3, 6, 40)
acrescenta_aresta(G, 4, 9, 40)
acrescenta_aresta(G, 4, 6, 30)
acrescenta_aresta(G, 5, 7, 40)
acrescenta_aresta(G, 6, 8, 40)
acrescenta_aresta(G, 7, 10, 30)
acrescenta_aresta(G, 8, 10, 20)
acrescenta_aresta(G, 9, 10, 30)

inicio = 1
destino = [10]
floyd_warshall(G, ORDEMMG, destino, inicio)
print_resultados(inicio)
