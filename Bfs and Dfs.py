from collections import deque
import networkx as nx
import matplotlib.pyplot as plt


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.append(node) if False else None
            visited.add(node)
            result.append(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)

    return result


def dfs(graph, start):
    visited = set()
    stack = [start]
    result = []

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            result.append(node)

            for neighbour in reversed(graph[node]):
                if neighbour not in visited:
                    stack.append(neighbour)

    return result


graph = {}

n = int(input("Enter number of nodes: "))

print("\nEnter node names:")
for i in range(n):
    node = input(f"Node {i+1}: ")
    graph[node] = []

graph_type = input("\nDirected or Undirected? (D/U): ").upper()

e = int(input("Enter number of edges: "))

if graph_type == "D":
    G = nx.DiGraph()
else:
    G = nx.Graph()

for node in graph:
    G.add_node(node)

print("\nEnter edges:")

for i in range(e):
    u = input("From: ")
    v = input("To: ")

    graph[u].append(v)
    G.add_edge(u, v)

    if graph_type == "U":
        graph[v].append(u)

print("\nAdjacency List")
for node in graph:
    print(node, ":", graph[node])

start = input("\nEnter starting node: ")

print("\nBFS Traversal:")
print(" -> ".join(bfs(graph, start)))

print("\nDFS Traversal:")
print(" -> ".join(dfs(graph, start)))

plt.figure(figsize=(8,6))
pos = nx.spring_layout(G)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=2000,
    node_color="skyblue",
    font_size=12,
    font_weight="bold",
    edge_color="black",
    arrows=(graph_type == "D")
)

plt.title("Graph Entered by User")
plt.show()