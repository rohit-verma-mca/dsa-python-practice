"""
Question:
Implement a Binary Search Tree class with insert and search methods,
plus an inorder method that returns the values in sorted order.

Topic     : Trees, Binary Search Tree
Source    : freeCodeCamp DSA Course
Difficulty: Medium
"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = TreeNode(value)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = TreeNode(value)
                    return
                current = current.right

    def search(self, value):
        current = self.root
        while current is not None:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def inorder(self):
        result = []

        def visit(node):
            if node is None:
                return
            visit(node.left)
            result.append(node.value)
            visit(node.right)

        visit(self.root)
        return result


if __name__ == "__main__":
    bst = BinarySearchTree()
    for v in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(v)

    print(bst.inorder())    # [20, 30, 40, 50, 60, 70, 80]
    print(bst.search(60))   # True
    print(bst.search(25))   # False