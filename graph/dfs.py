import matplotlib.pyplot as plt
from visualizer.animate import draw_graph

def dfs(graph, node, nodes, edges, positions, visited=None):
    if visited is None:
        visited = set()

    visited.add(node)
    draw_graph(nodes, edges, positions, visited, current=node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, nodes, edges, positions, visited)

if __name__ == "__main__":
    graph = {
        1: [2, 3],
        2: [4, 5],
        3: [6],
        4: [],
        5: [],
        6: []
    }

    nodes = list(graph.keys())
    edges = [(1,2),(1,3),(2,4),(2,5),(3,6)]
    positions = {
        1:(0,1), 2:(-1,0), 3:(1,0),
        4:(-1.5,-1), 5:(-0.5,-1), 6:(1,-1)
    }

    plt.figure(figsize=(6,5))
    dfs(graph, 1, nodes, edges, positions)
    plt.show()
