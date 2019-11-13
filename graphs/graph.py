# Graph representation using adjacency-list 
#


from collections import defaultdict


class Graph:

    class V:
        """ Vertex in the graph. """
        def __init__(self, v=None, edges=None):
            self.vertex = v
            self.edges = {} if edges is None else edges

        def __eq__(self, other):
            return hasattr(other, "vertex") and other.vertex == self.vertex

        def __hash__(self):
            return hash(self.vertex)

        def __repr__(self):
            return "{0} -> {1}".format(str(self.vertex), str([edge for _, edge in self.edges.items()]))

    class E:
        """ Edge between vertices. """
        def __init__(self, f, t, w=1):
            self.from_vertex = f
            self.to_vertex = t
            self.weight = w

        def __eq__(self, other):
            return hasattr(other, "to_vertex") and other.to_vertex == self.to_vertex

        def __hash__(self):
            return hash(self.to_vertex)

        def __repr__(self):
            return "{0}<{1}>".format(self.to_vertex, self.weight)

    def __init__(self, edges=None, directed=False):
        self._graph = defaultdict(Graph.V)
        self._directed = directed
        self.add_edges(edges)

    def add_edges(self, edges):
        if not edges:
            return
        for tpl in edges:
            if len(tpl) == 3:
                f, t, w = tpl
                self.add_edge(f, t, w)
            else:
                f, t = tpl
                self.add_edge(f, t)

    def add_edge(self, f, t, w=1):
        self._graph[f].vertex = f
        self._graph[f].edges[t] = Graph.E(f, t, w)

        if not self._directed:
            self._graph[t].vertex = t
            self._graph[t].edges[f] = Graph.E(t, f, w)
        else:
            self._graph[t].vertex = t

    def remove_edge(self, f, t):
        if f in self._graph:
            if t in self._graph[f].edges:
                del self._graph[f].edges[t]
                if not self._directed:
                    self.remove_edge(t, f)

    def remove_vertex(self, v):
        for _, vertex in self._graph.items():
            if v in vertex.edges:
                del vertex.edges[v]
        
        if v in self._graph:
            del self._graph[v]

    def edge(self, f, t):
        if f in self._graph:
            if t in self._graph[f].edges:
                return self._graph[f].edges[t]
        return None

    def vertex(self, v):
        if v in self._graph:
            return self._graph[v]
        return None

    def vertices(self):
        return [vertex for _, vertex in self._graph.items()]

    def __repr__(self):
        s = ""
        for _, vertex in self._graph.items():
            s += "{0}\n".format(vertex)
        return s


def test_cases():
    # --
    print("-- New unweighted graph: --")
    edges = [
        ("A", "B"),
        ("B", "C"),
        ("B", "D"),
        ("C", "D"),
        ("E", "F"),
        ("F", "C"),
    ]

    g = Graph(edges)
    print(g)

    g.remove_edge("B", "D")
    print("remove edge B -> D")
    print(g)

    g.remove_vertex("C")
    print("remove vertex C")
    print(g)

    # -- 
    print(" -- New weighted graph: --")
    wedges = [
        ("A", "B", 7),
        ("B", "C", 3),
        ("B", "D", 11),
        ("C", "D", 8),
        ("E", "F", 4),
        ("F", "C", 6),
    ]
    wg = Graph(wedges, True)
    print(wg)

    wg.remove_vertex("B")
    print("remove vertex B")
    print(wg)

    wg.add_edge("A", "D", 17)
    print("add edge A -> D")
    print(wg)

    wg.add_edge("F", "D", 2)
    print("add edge F -> D")
    print(wg)

    print("edge F -> C, weight: {0}\n".format(wg.edge("F", "C").weight))
    print("vertex F:  {0}\n".format(wg.vertex("F")))

if __name__ == "__main__":
    test_cases()