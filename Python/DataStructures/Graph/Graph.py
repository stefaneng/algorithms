class Graph(object):
    "(Undirected) Graph data structure (using Adjacency Lists implemented with a dict)"
    def __init__(self):
        self.adj = {}

    def insert_vertex(self, v):
        "Inserts vertex `x` into the graph"
        if v not in self.adj:
            self.adj[v] = []
        return self.adj[v]

    def insert_edge(self, u, v):
        self.insert_vertex(u)
        self.insert_vertex(v)
        self.adj[u].append(v)
        self.adj[v].append(u)
