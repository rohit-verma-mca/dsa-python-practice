"""
Question:
Write a recursive function that returns the height of a binary tree
(the number of nodes along the longest path from the root down to a
leaf). An empty tree has height 0.

Topic     : Trees, Recursion
Source    : freeCodeCamp DSA Course
Difficulty: Easy
"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print(height(root))   # 3
    print(height(None))   # 0