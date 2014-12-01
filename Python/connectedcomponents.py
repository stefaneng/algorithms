from DataStructures import Graph, DisjointSet

def connected_components(g):
    "Returns a list of sets of connected components"
    ds = DisjointSet()
    for v in g.vertices():
        ds.make_set(v)
    for u,v in g.edges():
        if ds.find_set(u) != ds.find_set(v):
            ds.union(u,v)
    return ds

if __name__ == '__main__':
    g = Graph()
    g.insert_edge(1,2)
    g.insert_edge(1,3)
    g.insert_edge(4,5)
    g.insert_edge(5,9)
    print connected_components(g)
