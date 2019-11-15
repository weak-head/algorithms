# Topological sort

from dfs import DFS
from collections import deque

class TopologicalSort(DFS):

    def topological_sort(self, f):
        sorted_vertices = deque()
        self.dfs(on_finished=lambda v: sorted_vertices.appendleft(v))
        map(f, sorted_vertices)

if __name__ == "__main__":

    edges = [
        ("undershorts", "pants"),
        ("undershorts", "shoes"),
        ("socks", "shoes"),
        ("pants", "shoes"),
        ("pants", "belt"),
        ("belt", "jacket"),
        ("shirt", "belt"),
        ("shirt", "tie"),
        ("tie", "jacket")
    ]

    vertices = [
        "watch",
    ]

    # --

    def showv(v):
        print(v.vertex)

    g = TopologicalSort(edges, directed=True)
    g.add_vertices(vertices)

    print(" - Precedence among events: garments put on order - ")
    print(g)

    print(" - Topological sort: ")
    g.topological_sort(showv)

    # -- 

    edges = [
        ("m", "q"),
        ("m", "r"),
        ("m", "x"),
        ("q", "t"),
        ("n", "q"),
        ("n", "u"),
        ("n", "o"),
        ("u", "t"),
        ("r", "u"),
        ("r", "y"),
        ("y", "v"),
        ("o", "r"),
        ("o", "v"),
        ("o", "s"),
        ("v", "x"),
        ("v", "w"),
        ("s", "r"),
        ("p", "s"),
        ("p", "o"),
        ("p", "z"),
        ("w", "z"),
    ]

    g = TopologicalSort(edges, directed=True)
    print("\n\n - DAG - ")
    print(g)

    print(" - Topological sort: ")
    g.topological_sort(showv)
