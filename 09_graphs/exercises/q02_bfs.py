"""
Question:
Write a function that traverses a graph breadth-first from a starting
vertex using a queue, returning the vertices in the order they were
visited.

Topic     : Graphs, BFS
Source    : freeCodeCamp DSA Course
Difficulty: Medium
"""

from collections import deque


def bfs(graph, start):
    visited = {start}
    order = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


if __name__ == "__main__":
    graph = {
        0: [1, 2],
        1: [0, 3],
        2: [0, 3],
        3: [1, 2, 4],
        4: [3],
    }
    print(bfs(graph, 0))  # [0, 1, 2, 3, 4]