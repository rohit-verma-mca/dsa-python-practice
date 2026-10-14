"""
Question:
Write a function that checks whether a given binary tree is a valid
binary search tree. Checking only each node's immediate children is
not enough: every node must stay within the bounds set by all of its
ancestors.

Topic     : Trees, Binary Search Tree, Recursion
Source    : freeCodeCamp DSA Course
Difficulty: Medium
"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def is_valid_bst(node, low=float("-inf"), high=float("inf")):
    if node is None:
        return True

    if not (low < node.value < high):
        return False

    return (is_valid_bst(node.left, low, node.value) and
            is_valid_bst(node.right, node.value, high))


if __name__ == "__main__":
    # Valid BST
    #     2
    #    / \
    #   1   3
    valid = TreeNode(2)
    valid.left = TreeNode(1)
    valid.right = TreeNode(3)
    print(is_valid_bst(valid))    # True

    # Invalid BST: 3 sits in the right subtree of 5, but is smaller than 5
    #     5
    #    / \
    #   1   6
    #      / \
    #     3   7
    invalid = TreeNode(5)
    invalid.left = TreeNode(1)
    invalid.right = TreeNode(6)
    invalid.right.left = TreeNode(3)
    invalid.right.right = TreeNode(7)
    print(is_valid_bst(invalid))  # False