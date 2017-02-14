from practicalPython3.graph import *
from practicalPython3.graph_io import *

def opengraph(name):
    with open(name) as file:
        G = load_graph(file)
    return G

def computecomplement(G):
    H = Graph(False, 0)
    for V in G.vertices:
        H.add_vertex(Vertex(H,str(V)))
    print(H)
    for i in range(len(G.vertices) - 1):
        for j in range(len(G.vertices) - 1):
            if G.vertices[i] != G.vertices[j] and not G.is_adjacent(G.vertices[i],G.vertices[j]):
                H += Edge(H.vertices[i],H.vertices[j])
    print(H)

computecomplement(opengraph('examplegraph.gr'))