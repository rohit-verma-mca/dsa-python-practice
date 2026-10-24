"""
Question:
Write a function that finds the shortest path (fewest edges) between
two vertices in an unweighted graph using BFS, returning the path as
a list of vertices, or None if no path exists.

Topic     : Graphs, BFS
Source    : freeCodeCamp DSA Course
Difficulty: Medium
"""

from collections import deque


def shortest_path(graph, start, end):
    parent = {start: None}
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node == end:
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1]

        for neighbor in graph[node]:
            if neighbor not in parent:
                parent[neighbor] = node
                queue.append(neighbor)

    return None


if __name__ == "__main__":
    graph = {
        0: [1, 2],
        1: [0, 3],
        2: [0, 3],
        3: [1, 2, 4],
        4: [3],
    }
    print(shortest_path(graph, 0, 4))  # [0, 1, 3, 4]
    print(shortest_path(graph, 0, 0))  # [0]