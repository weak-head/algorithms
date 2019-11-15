# Depth-first search

from graph import Graph

class DFS(Graph):

    def dfs(self, f):
        """
        Depth-first search for both directed and undirected graphs,
        that classifies edges and assigns the discovered and finished time
        to the vertices.

        Directed graphs could have the following edges:
            - tree
            - back
            - forward
            - cross

        Undirected graphs could have the following edges:
            - tree
            - back
        """
        for vertex in self.vertices():
            vertex.color = "white"

        t = 1
        for vertex in self.vertices():
            if vertex.color == "white":
                t = self._dfs(vertex, t, f)

    def _dfs(self, vertex, t, f):
        vertex.discovered = t
        vertex.color = "grey"
        t = t + 1

        for _, edge in vertex.edges.items():
            v = self.vertex(edge.to_vertex)
            if v.color == "white":
                edge.type = "tree"
                t = self._dfs(v, t, f)
            elif v.color == "grey":
                # facing a "grey" edge in undirected graph
                # could mean that we are looking
                # at the "tree" edge or at the "back" edge
                if self._directed:
                    edge.type = "back"
                else:
                    # in an undirected graph the edges (v, u) and (u, v)
                    # are basically the same edge, so in case if we have already
                    # classified the edge (v, u) we should apply the same
                    # classification to the edge (u, v)
                    symmetrical_edge = self.edge(edge.to_vertex, edge.from_vertex)
                    if hasattr(symmetrical_edge, "type"):
                        edge.type = symmetrical_edge.type
                    else:
                        edge.type = "back"
            elif v.color == "black":
                # undirected graph doesn't have "forward" and "cross" edges
                # they are always "back" edges
                if self._directed:
                    edge.type = "forward" if vertex.discovered < v.discovered else "cross"
                else:
                    edge.type = "back"

        vertex.finished = t
        vertex.color = "black"
        f(vertex)
        return t + 1


if __name__ == "__main__":
    edges = [
        ("q", "s"),
        ("s", "v"),
        ("v", "w"),
        ("w", "s"),
        ("q", "w"),
        ("q", "t"),
        ("t", "x"),
        ("x", "z"),
        ("z", "x"),
        ("t", "y"),
        ("y", "q"),
        ("r", "u"),
        ("r", "y"),
        ("u", "y"),
    ]

    def vprint(vertex):
        print("{0} ({1} | {2})".format(vertex.vertex, vertex.discovered, vertex.finished))

    # --

    g = DFS(edges, directed=True)
    print(" -- directed graph -- ")
    print(g)

    print(" -- DFS -- \n")
    print("vertex ( discovered | finished )")
    g.dfs(vprint)

    print("\nedges:")
    for e in g.edges(): 
        print("{0} -> {1} ({2})".format(e.from_vertex, e.to_vertex, e.type))

    # --

    ug = DFS(edges)
    print("\n\n -- undirected graph -- ")
    print(ug)

    print(" -- DFS -- \n")
    print("vertex ( discovered | finished )")
    ug.dfs(vprint)

    print("\nedges:")
    for e in ug.edges(): 
        print("{0} -> {1} ({2})".format(e.from_vertex, e.to_vertex, e.type))
