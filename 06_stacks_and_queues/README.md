# Stacks & Queues

**Source:** freeCodeCamp DSA Course

## Concepts covered
- Stack — Last In, First Out (LIFO): push, pop, peek
- Queue — First In, First Out (FIFO): enqueue, dequeue
- Implementing both using Python lists and `collections.deque`
- Common stack use cases: balanced parentheses, undo functionality, call stacks
- Common queue use cases: task scheduling, BFS (used later in Graphs)

## My Notes
A stack only lets you add/remove from one end (the top) — last item in is the first
one out, like a stack of plates. A queue only lets you add at one end and remove from
the other — first item in is the first one out, like a line of people. Python lists
work fine for a stack (`.append()`/`.pop()` are both O(1) from the end), but using a
plain list as a queue is slow (`.pop(0)` is O(n) since everything shifts) — `deque`
from `collections` is the right tool for a queue since both ends are O(1).

## Practice Questions
| # | Question | Status |
|---|----------|--------|
| 1 | Implement a Stack | ⬜ |
| 2 | Implement a Queue | ⬜ |
| 3 | Balanced Parentheses Checker | ⬜ |
| 4 | Reverse a String Using a Stack | ⬜ |
| 5 | Implement a Queue Using Two Stacks | ⬜ |
| 6 | Min Stack (Stack with O(1) Minimum Lookup) | ⬜ |

> Solved questions go in `exercises/` as `qXX_short_description.py`, following the format in [`EXERCISE_FORMAT.md`](../EXERCISE_FORMAT.md).