import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

nodes = ['Поштове відділення 1', 'Поштове відділення 2', 'Склад 1', 'Склад 2', 'Поштове відділення 3','Поштове відділення 4', 'Поштове відділення 5', 'Склад 3', 'Склад 4']
G.add_nodes_from(nodes)

edges = [
    ('Поштове відділення 1', 'Склад 1'),
    ('Поштове відділення 1', 'Склад 2'),
    ('Поштове відділення 1', 'Склад 3'),
    ('Поштове відділення 2', 'Склад 1'),
    ('Склад 1', 'Склад 2'),
    ('Склад 2', 'Поштове відділення 3'),
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


def dfs(graph, start, goal, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == goal:
        return path
    for node in graph.neighbors(start):
        if node not in path:
            newpath = dfs(graph, node, goal, path)
            if newpath:
                return newpath
    return None

def bfs(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                return path + [next]
            else:
                queue.append((next, path + [next]))
    return None

start_node = 'Поштове відділення 1'
goal_node = 'Поштове відділення 3'

dfs_path = dfs(G, start_node, goal_node)
bfs_path = bfs(G, start_node, goal_node)


print(dfs_path)
print(bfs_path)

#DFS шукає глибоко, і може пройти довший шлях, оскільки він не зупиняється, поки не досягне кінцевої точки
#BFS навпаки, знаходить шлях за мінімум кроків, оскільки досліджує всі вузли на кожному рівні одночасно. Тому він краще коли необхідно знайти найкоротший шлях за кількістю кроків