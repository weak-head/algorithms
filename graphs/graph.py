# Graph representation using adjacency-list 
#


from collections import defaultdict


class Graph:

    class V:
        def __init__(self, v, w=1):
            self.vertex = v
            self.weight = w

        def __eq__(self, other):
            return hasattr(other, "vertex") and other.vertex == self.vertex

        def __hash__(self):
            return hash(self.vertex)

        def __repr__(self):
            if self.weight is None:
                return "{0}".format(self.vertex)
            else:
                return "{0}[{1}]".format(self.vertex, self.weight)


    def __init__(self, edges=None, directed=False):
        self._graph = defaultdict(set)
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
        self._graph[Graph.V(f, None)].add(Graph.V(t, w))
        if not self._directed:
            self._graph[Graph.V(t, None)].add(Graph.V(f, w))
        else:
            self._graph[Graph.V(t, None)]

    def remove_edge(self, f, t):
        if Graph.V(f) in self._graph:
            if Graph.V(t) in self._graph[Graph.V(f)]:
                self._graph[Graph.V(f)].remove(Graph.V(t))
                # if len(self._graph[Graph.V(f)]) == 0:
                    # del self._graph[Graph.V(f)]
                if not self._directed:
                    self.remove_edge(t, f)
        pass

    def remove_vertex(self, v):
        for _, edges in self._graph.items():
            if Graph.V(v) in edges:
                edges.remove(Graph.V(v))
        
        if Graph.V(v) in self._graph:
            del self._graph[Graph.V(v)]

    def edge(self, f, t):
        if Graph.V(f) in self._graph:
            # if Graph.V(t) in self._graph[Graph.V(f)]:
                # return self._graph[Graph.V(f)][Graph.V(t)])
            for edge in self._graph[Graph.V(f)]:
                if edge == Graph.V(t):
                    return edge
        return None

    def __repr__(self):
        s = ""
        for vertex, edges in self._graph.items():
            s += "{0} -> {1}\n".format(str(vertex), str(edges))
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
    print("add edge A -> B")
    print(wg)

    wg.add_edge("F", "D", 2)
    print("add edge F -> D")
    print(wg)

    print("edge F -> C, weight: {0}\n".format(wg.edge("F", "C").weight))

if __name__ == "__main__":
    test_cases()