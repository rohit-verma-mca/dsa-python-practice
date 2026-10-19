"""
Question:
Write a function that inverts (mirrors) a binary tree by swapping the
left and right children of every node, and returns the root.

Topic     : Trees, Recursion
Source    : freeCodeCamp DSA Course
Difficulty: Easy
"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inorder(node):
    if node is None:
        return []
    return inorder(node.left) + [node.value] + inorder(node.right)


def invert_tree(node):
    if node is None:
        return None

    node.left, node.right = invert_tree(node.right), invert_tree(node.left)
    return node


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print(inorder(root))         # [4, 2, 5, 1, 3]
    invert_tree(root)
    print(inorder(root))         # [3, 1, 5, 2, 4]