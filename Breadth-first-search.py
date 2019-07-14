from queue import Queue
from sys import argv
from maze import *

def BFS(G, start, end):
    for v in G.vertices:
        v.discovered = False
    Q = Queue()
    start.discovered = True
    Q.put(start)
    while not Q.empty():
        v = Q.get()
        if v == end:
            return True
        for edge in v.edges:
            if edge != None and not edge.discovered:
                edge.discovered = True
                edge.prev = v
                Q.put(edge)
    
    return False

if __name__ == '__main__':
    if len(argv) < 2:
        print("No Maze provided")
    else:
        m = maze(sys.argv[1])
        BFS(m.graph, m.start, m.end)
        m.path = reconstruct(m.graph, m.end)
        if len(argv) > 2: m.save(argv[2])
        else: m.save()