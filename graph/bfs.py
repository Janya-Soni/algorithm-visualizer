from collections import deque
import matplotlib.pyplot as plt
from visualizer.animate import draw_graph

def bfs(graph, start, nodes, edges, positions):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        draw_graph(nodes, edges, positions, visited, current=node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

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
    bfs(graph, 1, nodes, edges, positions)
    plt.show()
