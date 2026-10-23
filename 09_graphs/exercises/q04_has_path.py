"""
Question:
Given an undirected graph and two vertices, write a function that
returns True if there is any path connecting them, and False
otherwise.

Topic     : Graphs, DFS
Source    : freeCodeCamp DSA Course
Difficulty: Medium
"""


def has_path(graph, start, end):
    visited = {start}
    stack = [start]

    while stack:
        node = stack.pop()
        if node == end:
            return True
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

    return False


if __name__ == "__main__":
    # Two separate groups: {0, 1, 2} and {3, 4}
    graph = {
        0: [1],
        1: [0, 2],
        2: [1],
        3: [4],
        4: [3],
    }
    print(has_path(graph, 0, 2))  # True
    print(has_path(graph, 0, 4))  # False