# Реалізація алгоритму Дейкстри для знаходження найкоротшого шляху між усіма парами вершин у графі

import networkx as nx
import matplotlib.pyplot as plt
import random

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


# Додаємо ваги до ребер
for (u, v) in G.edges():
    G[u][v]['weight'] = random.randint(1, 10)

# Перетворюємо граф у формат словника, який потрібен для алгоритму Дейкстри

def convert_to_dict_format(G):
    graph_dict = {}
    for node in G.nodes():
        # Для кожної вершини у графі створюємо відповідний словник
        # де ключ - це сусідня вершина, а значення - вага ребра
        graph_dict[node] = {neighbor: G[node][neighbor]['weight'] for neighbor in G.neighbors(node)}
    return graph_dict

# Конвертуємо граф
graph_dict_format = convert_to_dict_format(G)

# Функція Дейкстри
def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])
        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        unvisited.remove(current_vertex)

    return distances

# Застосування алгоритму Дейкстри для кожної вершини
all_pairs_shortest_paths = {node: dijkstra(graph_dict_format, node) for node in graph_dict_format}

# Виведення результатів
for start_node, paths in all_pairs_shortest_paths.items():
    print(f"Найкоротші шляхи від {start_node}:")
    for end_node, path_length in paths.items():
        print(f"До {end_node}: {path_length}")
    print()

