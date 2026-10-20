# Graphs

**Source:** freeCodeCamp DSA Course

## Concepts covered
- Graph terminology: vertex, edge, neighbor, directed vs undirected
- Adjacency list representation
- Breadth-first search (BFS) using a queue
- Depth-first search (DFS) using recursion or a stack
- Tracking visited nodes to avoid infinite loops on cycles
- Connected components and shortest path in an unweighted graph

## My Notes
A graph is a set of vertices connected by edges. Unlike a tree, a graph can have
cycles, so every traversal needs a `visited` set or it can loop forever. BFS explores
level by level using a queue, which is why it finds the shortest path in an unweighted
graph: the first time it reaches a node is via the fewest edges. DFS goes as deep as it
can before backtracking, using recursion or a stack. Both visit every vertex and edge
once, so both are O(V + E).

## Practice Questions
| # | Question | Status |
|---|----------|--------|
| 1 | Build a Graph with an Adjacency List | ⬜ |
| 2 | Breadth-First Search (BFS) | ⬜ |
| 3 | Depth-First Search (DFS) | ⬜ |
| 4 | Check if a Path Exists | ⬜ |
| 5 | Count Connected Components | ⬜ |
| 6 | Shortest Path in an Unweighted Graph | ⬜ |

> Solved questions go in `exercises/` as `qXX_short_description.py`, following the format in [`EXERCISE_FORMAT.md`](../EXERCISE_FORMAT.md).