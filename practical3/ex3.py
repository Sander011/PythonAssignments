from practical3.graph import *
from practical3.graph_io import *
with open('examplegraph.gr') as g:
    G = load_graph(g)
with open('mygraph.dot', 'w') as f:
    write_dot(G, f)