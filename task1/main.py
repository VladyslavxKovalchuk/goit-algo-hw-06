import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

nodes = ['Поштове відділення 1', 'Поштове відділення 2', 'Склад 1', 'Склад 2', 'Поштове відділення 3','Поштове відділення 4', 'Поштове відділення 5', 'Склад 3', 'Склад 4']
G.add_nodes_from(nodes)

edges = [
    ('Поштове відділення 1', 'Склад 1'),
    ('Поштове відділення 1', 'Склад 2'),
    ('Поштове відділення 2', 'Склад 1'),
    ('Склад 1', 'Склад 2'),
    ('Склад 2', 'Поштове відділення 3'),
    ('Поштове відділення 1', 'Склад 3'),
    ('Поштове відділення 3', 'Склад 3'),
    ('Поштове відділення 4', 'Склад 1'),
    ('Поштове відділення 4', 'Склад 4'),
    ('Поштове відділення 5', 'Склад 2'),
    ('Склад 3', 'Склад 4'),
    ('Поштове відділення 5', 'Поштове відділення 1'),
]
G.add_edges_from(edges)

plt.figure(figsize=(10, 6))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, width=2)
plt.title('Мережа поштових відділень та складів')
plt.show()

num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree = dict(G.degree())


print(f'Кількість вершин: {num_nodes}')
print(f'Кількість ребер: {num_edges}')
print(f'Ступінь вершин:')
print(*degree,sep='\n')
