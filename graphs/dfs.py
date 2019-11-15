# Depth-first search

from graph import Graph

class DFS(Graph):

    def dfs(self, f):
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
                edge.type = "Tree"
                t = self._dfs(v, t, f)
            elif v.color == "grey":
                edge.type = "Back"
            elif v.color == "black":
                if vertex.discovered < v.discovered:
                    edge.type = "Forward"
                else:
                    edge.type = "Cross"

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

    g = DFS(edges, directed=True)
    print(" -- directed graph -- ")
    print(g)

    def vprint(vertex):
        print("{0} ({1} | {2})".format(vertex.vertex, vertex.discovered, vertex.finished))

    print(" -- DFS -- \n")
    print("vertex ( discovered | finished )")
    g.dfs(vprint)

    print("\nedges:")
    for e in g.edges(): 
        print("{0} -> {1} ({2})".format(e.from_vertex, e.to_vertex, e.type))