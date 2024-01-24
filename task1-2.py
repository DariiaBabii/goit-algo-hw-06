# Моделювання реальної мережі - наскільки тісно пов’язані найпотужніші корпорації

import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

G = nx.Graph()

# Додавання вершин і ребер
companies = ['Nike', 'Disney', 'Visa', 'Microsoft', 'Apple', 'General Electric',
             'McDonalds', 'Chevron', 'Intel', 'American Express', 'Walmart',
             'Exon Mobil', 'CAT', 'Boeing', 'Travelers', 'P&G', 'IBM', '3M', 'Coca Cola']

# Додавання вершин
G.add_nodes_from(companies)

# Додавання ребер
connections = [('Nike', 'Disney'), ('Disney', 'Visa'), ('Visa', 'Microsoft'),
               ('Apple', 'General Electric'), ('Apple', 'Nike'), ('Apple', 'Disney'),
               ('McDonalds', 'Chevron'), ('Apple', 'Chevron'), ('Chevron', 'McDonalds'),
               ('Intel', 'American Express'), ('Intel', 'Nike'),
               ('Walmart', 'Exon Mobil'), ('Exon Mobil', 'CAT'), ('CAT', 'Boeing'),('Disney', 'McDonalds'),
               ('Exon Mobil', 'Travelers'), ('Walmart', 'General Electric'),
               ('Travelers', 'Boeing'), ('CAT', 'Chevron'), ('Exon Mobil', 'American Express'),
               ('CAT', 'McDonalds'), ('P&G', 'American Express'), ('IBM', '3M'),
               ('P&G', 'IBM'), ('Boeing', '3M'), ('3M', 'Coca Cola'), ('Boeing', 'IBM'),
               ('3M', 'Chevron'), ('Boeing', 'American Express'), ('IBM', 'American Express')]

G.add_edges_from(connections)

# Малювання графа
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()

# Аналіз графа

# Кількість вершин
num_nodes = G.number_of_nodes()
print(f"Кількість вершин (компаній): {num_nodes}")

# Кількість ребер
num_edges = G.number_of_edges()
print(f"Кількість ребер (зв'язків між компаніями): {num_edges}")

# Ступені вершин
degrees = G.degree()
print("Ступінь кожної вершини:")
for company, degree in degrees:
    print(f"{company}: {degree}")

# Густина графа
density = nx.density(G)
print(f"Густина графа: {density:.4f}")


# Порівняння алгоритмів DFS і BFS для знаходження шляхів

def dfs_recursive(graph, vertex, path=None, visited=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    
    visited.add(vertex)
    path.append(vertex)

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, path, visited)
    return path

def bfs_iterative(graph, start):
    visited = set()
    queue = deque([(start, [start])])  # Зберігаємо шляхи разом із вершинами

    paths = []

    while queue:
        vertex, path = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)

            for neighbor in set(graph[vertex]) - visited:
                queue.append((neighbor, path + [neighbor]))
            
            paths.append(path)
    return paths

# Конвертуємо граф G в формат списку суміжності для наших алгоритмів
graph = {node: list(G.neighbors(node)) for node in G.nodes()}

# Застосування DFS
dfs_paths = dfs_recursive(graph, 'Nike')  # Припускаючи, що ми починаємо з 'Nike'

# Застосування BFS
bfs_paths = bfs_iterative(graph, 'Nike')

# Виведення результатів
print('-'*110)
print('\n')
print("DFS Paths:", dfs_paths)
print('\n')
print("BFS Paths:", bfs_paths)
