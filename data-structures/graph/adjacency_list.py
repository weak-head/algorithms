'''Graph implementation using adjacency list'''

class Graph:

    class Edge:
        def __init__(self, vertice=None, weight=None):
            self.vertice = vertice
            self.weight = weight

    def __init__(self, directed=False):
        self.edges = {}
        self.num_edges = 0
        self.directed = directed

    def insert_edge(self, from_vertice, to_vertice, weight=None, directed=False):
        if from_vertice not in self.edges:
            self.edges[from_vertice] = []

        edge = Graph.Edge(to_vertice, weight)
        self.edges[from_vertice].append(edge)
        self.num_edges = self.num_edges + 1

        if not self.directed and directed is False:
            self.insert_edge(to_vertice, from_vertice, weight, True)