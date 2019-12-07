from sys import argv
from maze import *

def Astar(G, start, end):
    Q = []
    for v in G.vertices:
        v.dist = float("inf")
        Q.append(v)
    
    start.dist = 0
    while len(Q) > 0:
        u = min(Q, key = lambda v: v.dist + Heuristic(v, end))
        
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

def Heuristic(v, u):
    return ((v.x - u.x)**2 + (v.y - u.y)**2)**.5

if __name__ == '__main__':
    if len(argv) < 2:
        print("No Maze provided")
    else:
        m = maze(argv[1])
        Astar(m.graph, m.start, m.end)
        m.path = reconstruct(m.graph, m.end)
        setpath()
        if len(argv) > 2: m.save(argv[2])
        else: m.save()