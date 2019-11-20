# Strongly connected components

from dfs import DFS
from collections import deque, defaultdict


class SCC(DFS):

    def scc(self):
        """Find strongly connected components in the graph"""
        q = deque()
        # topological sort gives us the order of vertices
        self.dfs(on_finished=lambda x: q.appendleft(x))
        return self._transposed_scc_dfs(q)

    def _transposed_scc_dfs(self, queue):
        """Consider the vertices in order of decreasing finish time"""
        transposed = SCC.transpose(self)

        for v in transposed.vertices():
            v.color = "white"

        time = 1
        tree = 0
        for v in queue:
            vertex = transposed.vertex(v.vertex)
            if vertex.color == "white":
                tree += 1
                time = transposed._dfs(vertex, time, tree, None, None)

        components = defaultdict(deque)
        for vertex in transposed.vertices():
            components[vertex.tree].appendleft(self.vertex(vertex.vertex))

        return components


if __name__ == "__main__":
    edges = [
        ("a", "b"),
        ("b", "e"),
        ("b", "c"),
        ("b", "f"),
        ("c", "d"),
        ("c", "g"),
        ("d", "c"),
        ("d", "h"),
        ("e", "a"),
        ("e", "f"),
        ("f", "g"),
        ("g", "f"),
        ("g", "h"),
        ("h", "h"),
    ]

    def print_scc(scc):
        for ix, components in scc.items():
            print("[{0}]:".format(ix))
            for vertex in components:
                print("  {0}".format(vertex))
            print("")

    g = SCC(edges, directed=True)
    print("-- Directed Graph: -- ")
    print(g)

    print("Transposed: ")
    print(SCC.transpose(g))

    print("Strongly connected components: ")
    print_scc(g.scc())