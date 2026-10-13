"""
Question:
Implement a TreeNode class, build a small binary tree by hand, and
write recursive functions for inorder, preorder, and postorder
traversal, each returning a list of values.

Topic     : Trees, Depth-First Traversal
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


def preorder(node):
    if node is None:
        return []
    return [node.value] + preorder(node.left) + preorder(node.right)


def postorder(node):
    if node is None:
        return []
    return postorder(node.left) + postorder(node.right) + [node.value]


if __name__ == "__main__":
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print(inorder(root))     # [4, 2, 5, 1, 3]
    print(preorder(root))    # [1, 2, 4, 5, 3]
    print(postorder(root))   # [4, 5, 2, 3, 1]