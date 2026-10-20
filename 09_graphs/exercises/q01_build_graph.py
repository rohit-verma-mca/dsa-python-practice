"""
Question:
Implement an undirected Graph class using an adjacency list (a dict
mapping each vertex to a list of its neighbors), with add_vertex,
add_edge, and neighbors methods.

Topic     : Graphs
Source    : freeCodeCamp DSA Course
Difficulty: Easy
"""


class Graph:
    def __init__(self):
        self.adjacency = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency:
            self.adjacency[vertex] = []

    def add_edge(self, a, b):
        self.add_vertex(a)
        self.add_vertex(b)
        self.adjacency[a].append(b)
        self.adjacency[b].append(a)

    def neighbors(self, vertex):
        return self.adjacency.get(vertex, [])


if __name__ == "__main__":
    g = Graph()
    for a, b in [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)]:
        g.add_edge(a, b)

    for vertex in g.adjacency:
        print(f"{vertex} -> {g.neighbors(vertex)}")
    # 0 -> [1, 2]
    # 1 -> [0, 3]
    # 2 -> [0, 3]
    # 3 -> [1, 2, 4]
    # 4 -> [3]