import heapq
import math
AIRPORTS = {
    'CWB': (-25.5333, -49.1806),  # Curitiba
    'GIG': (-22.8122, -43.2497),  # Rio de Janeiro/Galeão (Destino)
    'GRU': (-23.4356, -46.4731),  # São Paulo/Guarulhos
    'BSB': (-15.8692, -47.9217),  # Brasília
    'CNF': (-19.6322, -43.9719),  # Confins/Belo Horizonte
}
AIR_ROUTES = {
    'CWB': {'GRU': 100, 'CNF': 250},
    'GRU': {'CWB': 90, 'GIG': 150, 'BSB': 300},
    'CNF': {'GRU': 240, 'BSB': 180, 'GIG': 220},
    'BSB': {'GRU': 310, 'CNF': 190, 'GIG': 350},
    'GIG': {},
}


RAIO_TERRA_KM = 6371
# Ex: Custo médio estimado de tempo/combustível por km.
CUSTO_MINIMO_POR_KM = 0.5

# --- 2. Funções de Cálculo ---


def haversine(coord1, coord2):
    """Calcula Haversine"""
    lat1, lon1 = coord1
    lat2, lon2 = coord2

    # Converter graus para radianos
    lat1_rad, lon1_rad = math.radians(lat1), math.radians(lon1)
    lat2_rad, lon2_rad = math.radians(lat2), math.radians(lon2)

    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * \
        math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = RAIO_TERRA_KM * c
    return distance


def heuristic_function_h(node, destination):
    """
    Função Heurística Dinâmica h(n): Estima o custo restante até o destino.
    (Distância Haversine * Custo Base * Fator Vento Ajustado)
    """
    if node not in AIRPORTS or destination not in AIRPORTS:
        return float('inf')

    # 1. Distância Haversine (km)
    distance_km = haversine(AIRPORTS[node], AIRPORTS[destination])

    fator_vento = 1.0  # Fator neutro

    # Aprimoramento: Simule que a rota reta (Haversine) BSB -> GIG é favorável.
    if node == 'BSB' and destination == 'GIG':
        fator_vento = 0.95  # Estimativa de 5% de economia de custo/tempo.
    # Outro aprimoramento: Simule que a rota reta CWB -> BSB é desfavorável.
    elif node == 'CWB' and destination == 'BSB':
        fator_vento = 1.05  # Estimativa de 5% de custo/tempo adicional.

    estimated_cost = distance_km * CUSTO_MINIMO_POR_KM * fator_vento

    return estimated_cost

# Algoritmo A*


def a_star_search(start_node, goal_node):

    open_set = [(0, start_node)]

    # g_score: Custo do caminho mais barato do início até o nó n (custo real)
    g_score = {airport: float('inf') for airport in AIRPORTS}
    g_score[start_node] = 0

    # f_score: Custo estimado total (g_score + h(n))
    f_score = {airport: float('inf') for airport in AIRPORTS}
    f_score[start_node] = heuristic_function_h(start_node, goal_node)
    came_from = {}

    while open_set:
        # Pega o nó na fila com o menor f_score
        current_f, current_node = heapq.heappop(open_set)

        if current_node == goal_node:
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start_node)
            return path[::-1], g_score[goal_node]

        # Explora os vizinhos (rotas de saída)
        for neighbor, cost in AIR_ROUTES.get(current_node, {}).items():
            # Custo do novo caminho do início para o vizinho
            tentative_g_score = g_score[current_node] + cost

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current_node
                g_score[neighbor] = tentative_g_score

                # f(n) = g(n) + h(n)
                f_score[neighbor] = tentative_g_score + \
                    heuristic_function_h(neighbor, goal_node)

                # Adiciona o vizinho à fila de prioridade
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None, float('inf')


start = 'CWB'
goal = 'GIG'

path, total_cost = a_star_search(start, goal)

print(f"--- Algoritmo A* com Heurística Dinâmica ---")
print(f"Origem: {start} | Destino: {goal}")
print("-" * 40)

if path:
    print(f"Caminho encontrado: {' -> '.join(path)}")
    print(f"Custo total (g(n)): {total_cost:.2f} unidades de custo")
else:
    print("Nenhum caminho encontrado.")
