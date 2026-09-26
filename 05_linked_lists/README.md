# Linked Lists

**Source:** freeCodeCamp DSA Course

## Concepts covered
- Node structure (value + pointer to next node)
- Singly linked lists — traversal, insertion, deletion
- Difference between a linked list and a Python list (array) under the hood
- Reversing a linked list
- Detecting cycles (Floyd's algorithm / "tortoise and hare")
- Finding the middle of a linked list

## My Notes
A linked list is built from individual "node" objects, each holding a value and a
pointer to the next node — unlike a Python list, there's no single contiguous block of
memory, so there's no direct indexing (`list[5]`); you have to walk from the head,
node by node, to reach any position. This makes insertion/deletion at the front O(1)
(no shifting needed, unlike an array), but random access is O(n) instead of O(1).

## Practice Questions
| # | Question | Status |
|---|----------|--------|
| 1 | Build a Linked List and Traverse It | ⬜ |
| 2 | Insert at Beginning, End, and Position | ⬜ |
| 3 | Delete a Node by Value | ⬜ |
| 4 | Find the Length of a Linked List | ⬜ |
| 5 | Reverse a Linked List | ⬜ |
| 6 | Find the Middle Node | ⬜ |
| 7 | Detect a Cycle | ⬜ |
| 8 | Merge Two Sorted Linked Lists | ⬜ |

> Solved questions go in `exercises/` as `qXX_short_description.py`, following the format in [`EXERCISE_FORMAT.md`](../EXERCISE_FORMAT.md).