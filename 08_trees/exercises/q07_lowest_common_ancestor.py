"""
Question:
Given a binary search tree and two values that both exist in it, find
their lowest common ancestor: the deepest node that has both values
in its subtree (a node can be its own ancestor).

Topic     : Trees, Binary Search Tree
Source    : freeCodeCamp DSA Course
Difficulty: Medium
"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root


def lowest_common_ancestor(root, p, q):
    current = root
    while current is not None:
        if p < current.value and q < current.value:
            current = current.left
        elif p > current.value and q > current.value:
            current = current.right
        else:
            return current.value  # the paths to p and q split here
    return None


if __name__ == "__main__":
    root = None
    for v in [6, 2, 8, 0, 4, 7, 9, 3, 5]:
        root = insert(root, v)

    print(lowest_common_ancestor(root, 2, 8))   # 6
    print(lowest_common_ancestor(root, 2, 4))   # 2
    print(lowest_common_ancestor(root, 3, 5))   # 4