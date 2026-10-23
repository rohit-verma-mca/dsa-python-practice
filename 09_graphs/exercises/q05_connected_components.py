"""
Question:
Write a function that counts the connected components in an
undirected graph (groups of vertices that are reachable from each
other but not from any vertex outside the group).

Topic     : Graphs, DFS
Source    : freeCodeCamp DSA Course
Difficulty: Medium
"""


def count_components(graph):
    visited = set()
    count = 0

    for node in graph:
        if node not in visited:
            count += 1
            visited.add(node)
            stack = [node]

            while stack:
                current = stack.pop()
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)

    return count


if __name__ == "__main__":
    graph = {
        0: [1],
        1: [0, 2],
        2: [1],
        3: [4],
        4: [3],
        5: [],  # an isolated vertex counts as its own component
    }
    print(count_components(graph))  # 3