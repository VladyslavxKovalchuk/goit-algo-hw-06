import networkx as nx
import matplotlib.pyplot as plt


def dijkstra(graph:nx.Graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.nodes.keys())

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, data in graph[current_vertex].items():
            weight = data['weight']
            distance = distances[current_vertex] + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance

        unvisited.remove(current_vertex)

    return distances

G = nx.Graph()

nodes = ['Поштове відділення 1', 'Поштове відділення 2', 'Склад 1', 'Склад 2', 'Поштове відділення 3','Поштове відділення 4', 'Поштове відділення 5', 'Склад 3', 'Склад 4']
G.add_nodes_from(nodes)


edges = {
    ('Поштове відділення 1', 'Склад 1'): 5,
    ('Поштове відділення 1', 'Склад 2'): 3,
    ('Поштове відділення 1', 'Склад 3'): 7,
    ('Поштове відділення 2', 'Склад 1'): 4,
    ('Склад 1', 'Склад 2'): 1,
    ('Склад 2', 'Поштове відділення 3'): 6,
    ('Поштове відділення 3', 'Склад 3'): 2,
    ('Поштове відділення 4', 'Склад 1'): 3,
    ('Поштове відділення 4', 'Склад 4'): 8,
    ('Поштове відділення 5', 'Склад 2'): 2,
    ('Склад 3', 'Склад 4'): 5,
    ('Поштове відділення 5', 'Поштове відділення 1'): 9,
}

G.add_edges_from(edges.keys())
nx.set_edge_attributes(G,edges, 'weight')

plt.figure(figsize=(10, 6))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, width=2)
plt.title('Мережа поштових відділень та складів')
plt.show()

shortest_paths = {}
for node in G.nodes:
    shortest_paths[node] = dijkstra(G, node)
print(*shortest_paths,sep=' -> ')