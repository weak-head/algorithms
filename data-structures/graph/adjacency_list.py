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
            raise Exception("The vertice doesn't exist")

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

    def dfs(self, start,
            process_vertex_early=None,
            process_vertex_late=None,
            process_edge=None):
        '''Depth-First Search'''

        if start not in self.edges:
            raise Exception("The vertice doesn't exist")

        time = 0
        state = {}
        for v in self.edges.keys():
            state[v] = SimpleNamespace()
            state[v].discovered = False
            state[v].processed = False
            state[v].parent = None
            state[v].entry_time = 0
            state[v].exit_time = 0

        def do_dfs(vertice):
            nonlocal time, state
            time = time + 1

            state[vertice].discovered = True
            state[vertice].entry_time = time

            if process_vertex_early is not None:
                process_vertex_early(vertice)

            for children in self.edges[vertice]:
                if not state[children].discovered:
                    state[children].parent = vertice

                    if process_edge is not None:
                        process_edge(vertice, children)

                    do_dfs(children)
                elif (not state[children].processed and state[children].parent != vertice) or self.directed:
                    process_edge(vertice, children)

            if process_vertex_late is not None:
                process_vertex_late(vertice)

            time = time + 1
            state[vertice].processed = True
            state[vertice].exit_time = time

        do_dfs(start)
        return state

    def two_color(self):
        '''Assigns Black or White label to each vertice of the graph'''

        colors = {v: 'uncolored' for v in self.edges.keys()}
        bipartite = True

        def complement(color):
            if color == 'uncolored':
                return 'uncolored'

            # return 'black' if color == 'white' else 'white'

        def process_edge(from_vertice, to_vertice):
            if colors[from_vertice] == colors[to_vertice]:
                nonlocal bipartite
                bipartite = False

            colors[to_vertice] = complement(colors[from_vertice])

        for vertice in self.edges.keys():
            if colors[vertice] == 'uncolored':
                colors[vertice] = 'white'
                self.bfs(vertice, process_edge=process_edge)

        return bipartite, colors


