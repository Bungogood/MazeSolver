from sys import argv
from maze import *

def Dijkstra(G, start, end):
    Q = []
    for v in G.vertices:
        v.dist = float("inf")
        Q.append(v)
    
    start.dist = 0
    while len(Q) > 0:
        u = min(Q, key = lambda v: v.dist)
        
        if u == end:
            return True
        
        Q.remove(u)
        for edge in u.edges:
            if edge != None:
                alt = u.dist + 1
                if alt < edge.dist:
                    edge.dist = alt
                    edge.prev = u
    
    return False

if __name__ == '__main__':
    if len(argv) < 2:
        print("No Maze provided")
    else:
        m = maze(argv[1])
        Dijkstra(m.graph, m.start, m.end)
        m.path = reconstruct(m.graph, m.end)
        m.setpath()
        if len(argv) > 2: m.save(argv[2])
        else: m.save()