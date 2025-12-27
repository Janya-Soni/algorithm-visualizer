import matplotlib.pyplot as plt
from tree.tree_node import TreeNode
from visualizer.animate import draw_tree

def inorder(root, full_tree):
    if root is None:
        return

    inorder(root.left, full_tree)

    plt.clf()
    draw_tree(full_tree, highlight=root)
    plt.axis("off")
    plt.pause(0.8)

    inorder(root.right, full_tree)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    plt.figure(figsize=(8, 6))
    inorder(root, root)
    plt.show()
