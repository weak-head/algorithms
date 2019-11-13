# Breadth-first search

from graph import Graph
from collections import deque

class Bfs(Graph):

    def bfs(self, root, f):
        if root not in self._graph:
            return

        for v in self.vertices():
            v.color = "white"

        v = self.vertex(root)
        v.color = "black"
        v.distance = 0

        q = deque([v])
        while len(q) != 0:
            v = q.popleft()
            f(v)

            for _, edge in v.edges.items():
                nv = self.vertex(edge.to_vertex)
                if nv.color == "white":
                    nv.color = "black"
                    nv.distance = v.distance + edge.weight
                    q.append(nv)


if __name__ == "__main__":
    edges = [
        ("A", "B"),
        ("A", "C"),
        ("A", "D"),
        ("B", "K"),
        ("B", "E"),
        ("C", "E"),
        ("C", "F"),
        ("C", "G"),
        ("G", "H"),
        ("K", "L"),
        ("L", "M"),
        ("M", "D"),
    ]

    g = Bfs(edges)
    print(g)

    def printv(v):
        print("{0} -> {1}".format(v.distance, v.vertex))

    print(" -- bfs: A -- ")
    g.bfs("A", printv) 

    print("\n -- bfs: H -- ")
    g.bfs("H", printv) 

    print("\n\n -- Weighted graph -- \n")
    wedges = [
        ("A", "B", 3),
        ("A", "C", 7),
        ("A", "D", 4),
        ("B", "K", 9),
        ("B", "E", 8),
        ("C", "E", 6),
        ("C", "F", 11),
        ("C", "G", 8),
        ("G", "H", 13),
        ("K", "L", 3),
        ("L", "M", 10),
        ("M", "D", 7),
    ]

    wg = Bfs(wedges)
    print(wg)

    print(" -- bfs: A -- ")
    wg.bfs("A", printv) 

    print("\n -- bfs: H -- ")
    wg.bfs("H", printv) 