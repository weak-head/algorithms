# Depth-first search

from graph import Graph

class DFS(Graph):

    def dfs(self, on_discovered=None, on_finished=None):
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

        time = 1
        tree = 0
        for vertex in self.vertices():
            if vertex.color == "white":
                tree += 1
                time = self._dfs(vertex, time, tree, on_discovered, on_finished)

    def _dfs(self, vertex, time, tree, on_discovered, on_finished):
        vertex.discovered = time
        vertex.tree = tree
        vertex.color = "grey"
        if on_discovered is not None:
            on_discovered(vertex)
        time = time + 1

        for _, edge in vertex.edges.items():
            v = self.vertex(edge.to_vertex)
            if v.color == "white":
                edge.type = "tree"
                time = self._dfs(v, time, tree, on_discovered, on_finished)
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

        vertex.finished = time
        vertex.color = "black"
        if on_finished is not None:
            on_finished(vertex)
        return time + 1


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
        print("{0} ({1} | {2}) [{3}]".format(vertex.vertex, vertex.discovered, vertex.finished, vertex.tree))

    # --

    g = DFS(edges, directed=True)
    print(" -- directed graph -- ")
    print(g)

    print(" -- DFS -- \n")
    print("vertex ( discovered | finished ) [tree]")
    g.dfs(on_finished=vprint)

    print("\nedges:")
    for e in g.edges(): 
        print("{0} -> {1} ({2})".format(e.from_vertex, e.to_vertex, e.type))

    # --

    ug = DFS(edges)
    print("\n\n -- undirected graph -- ")
    print(ug)

    print(" -- DFS -- \n")
    print("vertex ( discovered | finished )")
    ug.dfs(on_finished=vprint)

    print("\nedges:")
    for e in ug.edges(): 
        print("{0} -> {1} ({2})".format(e.from_vertex, e.to_vertex, e.type))
