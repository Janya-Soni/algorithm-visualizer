from collections import deque
import matplotlib.pyplot as plt
from visualizer.animate import draw_graph

def shortest_path(graph, start, end, nodes, edges, positions):
    queue = deque([[start]])
    visited = set([start])

    while queue:
        path = queue.popleft()
        node = path[-1]

        draw_graph(nodes, edges, positions, visited, current=node, path=path)

        if node == end:
            return path

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])

if __name__ == "__main__":
    graph = {
        1: [2, 3],
        2: [4],
        3: [4, 5],
        4: [6],
        5: [6],
        6: []
    }

    nodes = list(graph.keys())
    edges = [(1,2),(1,3),(2,4),(3,4),(3,5),(4,6),(5,6)]
    positions = {
        1:(0,1), 2:(-1,0), 3:(1,0),
        4:(0,-1), 5:(2,-1), 6:(1,-2)
    }

    plt.figure(figsize=(6,6))
    shortest_path(graph, 1, 6, nodes, edges, positions)
    plt.show()
