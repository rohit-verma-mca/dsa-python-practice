"""
Question:
Write a recursive function that traverses a graph depth-first from a
starting vertex, returning the vertices in the order they were
visited.

Topic     : Graphs, DFS, Recursion
Source    : freeCodeCamp DSA Course
Difficulty: Medium
"""


def dfs(graph, node, visited=None, order=None):
    if visited is None:
        visited = set()
    if order is None:
        order = []

    visited.add(node)
    order.append(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, order)

    return order


if __name__ == "__main__":
    graph = {
        0: [1, 2],
        1: [0, 3],
        2: [0, 3],
        3: [1, 2, 4],
        4: [3],
    }
    print(dfs(graph, 0))  # [0, 1, 3, 2, 4]