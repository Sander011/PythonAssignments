
from practical3.graph_io import *

from util.graph import *
from practicalPython3.graph_io import *
from practicalPython3.graph import *

from util.graph_io import *

with open('examplegraph.gr') as f:
    G = load_graph(f)
print(G)
v = G.vertices[0]
w = G.vertices[2]
G.add_edge(Edge(v,w))
with open('examplegraph2.gr', 'w') as f:
    save_graph(G, f)