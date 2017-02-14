from collections import deque
from practicalPython3.ex1 import *
from practicalPython3.graph import *
from practicalPython3.graph_io import *


def bfs(G, v):
    queue = deque([G.vertices[0]])
    while queue:
        currentvertex = queue.popleft()
        for w in G.vertices:
            if G.is_adjacent(w, currentvertex):
                if w == v:
                    return True
                queue.append(w)
    return False

def dfs(G,v):
    stack = [G.vertices[0]]
    while stack:
        currentvertex = stack.pop()
        for w in G.vertices:
            if G.is_adjacent(w, currentvertex):
                if w == v:
                    return True
                stack.append(w)

def testconnected(G):
    for V in G.vertices:
        if not bfs(G, V):
            return False
    return True


def getdistance(G, v):
    if bfs(G, v):
        distance = 0
        current = v
        while current != G.vertices[0]:
            found = False

            for w in G.vertices:
                if not found:
                    if G.is_adjacent(current, w):
                        if G.find_edge(current, w).pop().weight == None:
                            distance += 1
                        else:
                            distance += G.find_edge(current, w).pop().weight
                        current = w
                        found = True

    return distance


def labelvertices(G):
    count = 0
    done = []
    done.append(G.vertices[0])
    queue = deque([G.vertices[0]])
    v = G.vertices[len(G.vertices) - 1]
    while queue and count < len(G.vertices):
        currentvertex = queue.popleft()
        # found = False
        for w in G.vertices:
            # if not found:
                if G.is_adjacent(currentvertex, w) and done.__contains__(w):
                    print(w)
                    w.label = count
                    count += 1
                    queue.append(w)
                    done.append(w)
                    # found = True
    return G


G = creategraphcomplete(10)
# print(G)
# print(getdistance(G, G.vertices[8]))
print(labelvertices(G))
with open('examplegraph2.gr', 'w') as f:
    write_dot(labelvertices(G), f)
