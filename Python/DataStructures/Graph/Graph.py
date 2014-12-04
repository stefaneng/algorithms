from ..DisjointSet import DisjointSet

class Graph(object):
    "(Undirected) Graph data structure (using Adjacency Lists implemented with a dict)"
    def __init__(self):
        self.adj = {}

    def vertices(self):
        "Returns a list of vertices"
        return self.adj.keys()

    def edges(self):
        "Returns edges as a list of pairs [(u,v)]"
        edges = []
        for u,v_list in self.adj.iteritems():
            if v_list:
                for v in v_list:
                    e = (u,v)
                    edges.append(e)
        return edges

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

    def connected_components(self):
        "Returns a list of sets of connected components"
        ds = DisjointSet()
        for v in self.vertices():
            ds.make_set(v)
            for u,v in self.edges():
                if ds.find_set(u) != ds.find_set(v):
                    ds.union(u,v)
        return ds
