# Trees

**Source:** freeCodeCamp DSA Course

## Concepts covered
- Tree terminology: root, parent, child, leaf, height, depth
- Binary trees and binary search trees (BSTs)
- Depth-first traversals: inorder, preorder, postorder
- Breadth-first traversal (level-order) using a queue
- BST property: left subtree < node < right subtree
- Why BST search/insert is O(log n) on a balanced tree, but O(n) in the worst case

## My Notes
A tree is like a linked list where each node can point to more than one next node.
In a binary tree, each node has at most two children (left and right). Most tree
problems become simple once you think recursively: solve the problem for the left
subtree, solve it for the right subtree, then combine the results. A BST adds one rule
(everything on the left is smaller, everything on the right is larger), which is what
lets us search by discarding half the tree at each step, just like binary search on a
sorted list. Inorder traversal of a BST always gives the values in sorted order.

## Practice Questions
| # | Question | Status |
|---|----------|--------|
| 1 | Build a Binary Tree and Traverse It (DFS) | ⬜ |
| 2 | Level-Order Traversal (BFS) | ⬜ |
| 3 | Height of a Binary Tree | ⬜ |
| 4 | Implement a Binary Search Tree | ⬜ |
| 5 | Validate a Binary Search Tree | ⬜ |
| 6 | Count Total Nodes and Leaf Nodes | ⬜ |
| 7 | Lowest Common Ancestor in a BST | ⬜ |
| 8 | Invert a Binary Tree | ⬜ |

> Solved questions go in `exercises/` as `qXX_short_description.py`, following the format in [`EXERCISE_FORMAT.md`](../EXERCISE_FORMAT.md).