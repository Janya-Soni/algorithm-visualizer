import matplotlib.pyplot as plt

# ARRAY VISUALIZATION (Sorting Algorithms)

def draw_array(arr, highlight_indices=None, sorted_indices=None, pause_time=0.1):
    """
    Draws an array as bars.
    highlight_indices : indices being compared (red)
    sorted_indices   : indices already sorted (green)
    """
    plt.clf()

    colors = ["blue"] * len(arr)

    if sorted_indices:
        for i in sorted_indices:
            if 0 <= i < len(arr):
                colors[i] = "green"

    if highlight_indices:
        for i in highlight_indices:
            if 0 <= i < len(arr):
                colors[i] = "red"

    plt.bar(range(len(arr)), arr, color=colors)
    plt.pause(pause_time)

# TREE VISUALIZATION (Binary Trees)

def draw_tree(root, x=0, y=0, dx=1, highlight=None):
    """
    Draws a binary tree.
    highlight : node currently being visited
    """
    if root is None:
        return

    color = "red" if root == highlight else "lightblue"

    plt.text(
        x, y, str(root.value),
        ha="center", va="center",
        bbox=dict(boxstyle="circle", facecolor=color)
    )

    # Left child
    if root.left:
        plt.plot([x, x - dx], [y, y - 1], color="black")
        draw_tree(root.left, x - dx, y - 1, dx / 2, highlight)

    # Right child
    if root.right:
        plt.plot([x, x + dx], [y, y - 1], color="black")
        draw_tree(root.right, x + dx, y - 1, dx / 2, highlight)


# GRAPH VISUALIZATION (BFS, DFS, Shortest Path)


def draw_graph(nodes, edges, positions,
               visited=None, current=None, path=None, pause_time=0.8):
    """
    nodes     : list of nodes
    edges     : list of (u, v)
    positions : dict {node: (x, y)}
    visited   : set of visited nodes
    current   : current node being processed
    path      : final path (highlighted in green)
    """

    plt.clf()

    # Draw edges
    for u, v in edges:
        x1, y1 = positions[u]
        x2, y2 = positions[v]
        plt.plot([x1, x2], [y1, y2], color="black")

    # Draw nodes
    for node in nodes:
        x, y = positions[node]

        if path and node in path:
            color = "green"
        elif node == current:
            color = "red"
        elif visited and node in visited:
            color = "lightblue"
        else:
            color = "gray"

        plt.text(
            x, y, str(node),
            ha="center", va="center",
            bbox=dict(boxstyle="circle", facecolor=color)
        )

    plt.axis("off")
    plt.pause(pause_time)
