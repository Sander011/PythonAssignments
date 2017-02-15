from util.graph import *

def creategraphpath(n):
    G = Graph(False, n)
    for i in range(n-1):
        E = Edge(G.vertices[i], G.vertices[i+1])
        G += E
    return G

def creategraphcycle(n):
    G = Graph(False, n)
    for i in range(n-1):
        G += Edge(G.vertices[i], G.vertices[i+1])
    G += Edge(G.vertices[n-1], G.vertices[0])
    return G

def creategraphcomplete(n):
    G = Graph(False, n)
    for i in range(n):
        for j in range(i+1, n):
            G += Edge(G.vertices[i], G.vertices[j])
    return G

def add(G, H):
    I = Graph(False, 0)
    for V in G.vertices:
        I.add_vertex(V)
    for V in H.vertices:
        I.add_vertex(V)
    for E in G.edges:
        I.add_edge(E)
    for E in H.edges:
        I.add_edge(V)
    return I


creategraphpath(10)
creategraphcycle(10)
creategraphcomplete(10)