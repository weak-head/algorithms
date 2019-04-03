'''Graph implementation using adjacency list'''

from queue import Queue
from enum import Enum
from types import SimpleNamespace

class Graph:

    class VerticeState(Enum):
        undiscovered = 0
        discovered = 1
        processed = 2

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

    def bfs(self, start,
            process_vertex_early=None,
            process_vertex_late=None,
            process_edge=None):
        '''Breadth-First Search'''

        if start not in self.edges:
            raise Exception("The edge doesn't exist")

        que = Queue()
        que.put(start)

        state = {}
        for vertice in self.edges.keys():
            v_state = SimpleNamespace()
            v_state.discovered = False
            v_state.processed = False
            v_state.parent = None
            state[vertice] = v_state

        while not que.empty():
            current = que.get()
            state[current].processed = True

            # process the 'current' vertice before edge
            if process_vertex_early is not None:
                process_vertex_early(current)

            for child in self.edges[current]:
                # process the edge between 'current' and 'child'
                if not state[child].processed or self.directed:
                    if process_edge is not None:
                        process_edge(current, child)

                # the 'child' is not discovered yet, need to be processed
                if not state[child].discovered:
                    state[child].discovered = True
                    que.put(child)
                    state[child].parent = current

            # process the 'current' vertice after edge
            if process_vertex_late is not None:
                process_vertex_late(current)
