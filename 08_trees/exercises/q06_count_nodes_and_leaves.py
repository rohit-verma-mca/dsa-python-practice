"""
Question:
Write two recursive functions: one that counts all nodes in a binary
tree, and one that counts only the leaf nodes (nodes with no
children).

Topic     : Trees, Recursion
Source    : freeCodeCamp DSA Course
Difficulty: Easy
"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


def count_leaves(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return count_leaves(node.left) + count_leaves(node.right)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print(count_nodes(root))    # 5
    print(count_leaves(root))   # 3 (nodes 4, 5, and 3)