import random

def reconstruir_caminho(visitados: dict, vertice_final: str):
    """
    Reconstrói o caminho de um vértice inicial até um vértice final.

    Percorre o dicionário de vértices visitados, onde cada vértice mapeia para seu antecessor, 
    e reconstrói o caminho percorrido durante uma busca no grafo.

    Parameters
    ----------
    visitados : dict
        Um dicionário onde as chaves são os vértices visitados e os valores são seus antecessores.
    vertice_final : str
        O vértice final para o qual se deseja reconstruir o caminho.

    Returns
    -------
    list
        Uma lista de vértices que representam o caminho do vértice inicial (implícito em `visitados`) 
        até o vértice final. Caso o vértice final não seja alcançável, a lista estará vazia ou 
        conterá apenas o vértice final.

    Examples
    --------
    >>> visitados = {'B': 'A', 'C': 'B', 'D': 'C'}
    >>> reconstruir_caminho(visitados, 'D')
    ['A', 'B', 'C', 'D']

    >>> visitados = {'B': 'A', 'C': 'B', 'D': None}
    >>> reconstruir_caminho(visitados, 'D')
    ['D']
    """
    caminho = []
    atual = vertice_final    
    while atual is not None:
        caminho.append(atual)
        atual = visitados.get(atual)
    caminho.reverse()
    return caminho

def random_walk(visitados: dict, grafo: list, atual: int, antecessor: int, vertice_final: int, i: int, n: int):
    """
    Realiza um random walk para verificar a existência de um caminho entre dois vértices.

    Parameters
    ----------
    visitados : dict
        Dicionário que registra os vértices visitados como chaves e os índices de seus antecessores como valores.
    grafo : list
        Matriz de adjacência representando o grafo.
    atual : int
        Índice do vértice atual na busca.
    antecessor : int
        Índice do vértice anterior na busca. Para o vértice inicial, deve ser `None`.
    vertice_final : int
        Índice do vértice de destino na busca.
    i : int
        Contador de iterações da caminhada.
    n : int
        Número total de vértices no grafo.

    Returns
    -------
    tuple
        - bool: Indica se o vértice final foi encontrado (`True`) ou não (`False`).
        - dict: Dicionário `visitados` atualizado com os vértices explorados.
        - int: Número de iterações realizadas.

    Examples
    --------
    >>> grafo = [
    ...     [0, 1, 1, 0],
    ...     [1, 0, 0, 1],
    ...     [1, 0, 0, 1],
    ...     [0, 1, 1, 0]
    ... ]
    >>> visitados = {}
    >>> random_walk(visitados, grafo, 0, None, 3, 0, 4)
    (True, {0: None, 2: 0, 3: 2}, 2)
    """
    while i < (2*(n**3)):
        if atual not in visitados:
            visitados[atual] = antecessor

        vizinhos = [idx for idx, conectado in enumerate(grafo[atual]) if conectado == 1]
        if not vizinhos: 
            return False, visitados,i

        vizinho = random.choice(vizinhos)
        i += 1
        if vizinho == vertice_final:
            visitados[vizinho] = atual
            return True, visitados,i
        antecessor = atual
        atual = vizinho
    return False, visitados,i

def existe_caminho(grafo: list, vertice_inicial: str, vertice_final: str):
    """
    Verifica se existe um caminho entre dois vértices em um grafo.

    Parameters
    ----------
    grafo : list
        Matriz de adjacência representando o grafo.
    vertice_inicial : int
        Índice do vértice de origem.
    vertice_final : int
        Índice do vértice de destino.

    Returns
    -------
    tuple
        - bool: Indica se existe um caminho entre os vértices (`True`) ou não (`False`).
        - list: Caminho encontrado como uma lista de vértices, ou uma lista vazia se não houver caminho.
        - int: Número de iterações realizadas durante a busca.

    Examples
    --------
    >>> grafo = [
    ...     [0, 1, 1, 0],
    ...     [1, 0, 0, 1],
    ...     [1, 0, 0, 1],
    ...     [0, 1, 1, 0]
    ... ]
    >>> existe_caminho(grafo, 0, 3)
    (True, [0, 2, 3], 2)
    """
    if vertice_inicial < 0 or vertice_inicial >= len(grafo) or vertice_final < 0 or vertice_final >= len(grafo):
        return False, [], 0

    n = len(grafo)
    visitados = {}
    encontrado, visitados,i = random_walk(visitados, grafo, vertice_inicial, None, vertice_final, 0, n)

    if encontrado:
        caminho_indices = reconstruir_caminho(visitados, vertice_final)
        return True, caminho_indices, i
    else:
        return False, [], i

# Exemplo grafico de 100 vertices
def gerar_grafo_grande(n):
    """Função para gerar um grafo aleatório com `n` vértices e matriz de adjacência"""
    grafo = [[0] * n for _ in range(n)]  # Inicializa uma matriz de adjacência 0
    for i in range(n):
        for j in range(i + 1, n):  # Conexões são simétricas
            if random.random() < 0.1:  # 10% de chance de existir uma aresta entre i e j
                grafo[i][j] = 1
                grafo[j][i] = 1
    return grafo

# Gerando um grafo de 100 vértices
n = 100
grafo_grande = gerar_grafo_grande(n)

existe, caminho,i = existe_caminho(grafo_grande, 1, 58)
print("Existe caminho entre os vértices 1 e 58?", existe)
print("Caminho:", caminho)
print("interações:", i)

grafo = [
    [0, 1, 1, 0, 0, 0],  
    [1, 0, 0, 1, 1, 0],  
    [1, 0, 0, 0, 0, 1],  
    [0, 1, 0, 0, 0, 0],  
    [0, 1, 0, 0, 0, 1],  
    [0, 0, 1, 0, 1, 0]   
]
existe, caminho, i = existe_caminho(grafo, 0, 4)
print("Existe caminho entre os vértices 1 e 4?", existe)
print("Caminho:", caminho)
print("interações:", i)

grafo = [
    [0, 1, 0, 1, 0],  
    [1, 0, 1, 0, 0],  
    [0, 1, 0, 1, 0],  
    [1, 0, 1, 0, 0],  
    [0, 0, 0, 0, 0]
]
existe, caminho, i = existe_caminho(grafo, 0, 4)
print("Existe caminho entre os vértices 1 e 4?", existe)
print("Caminho:", caminho)
print("interações:", i)