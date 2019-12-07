from queue import Queue
from sys import argv
from maze import *

def DFS(G, start, end):
    for v in G.vertices:
        v.discovered = False
    
    return DFSrec(G, start,end)

def DFSrec(G, v, end):
    v.discovered = True
    
    if v == end:
        return True
    
    for edge in v.edges:
        if edge != None and not edge.discovered:
            edge.prev = v
            if DFSrec(G, edge, end): return True
    
    return False

'''
def DFS(G, start, end):
    for v in G.vertices:
        v.discovered = False
    
    Q = Queue()
    Q.put(start)
    while not Q.empty():
        v = Q.get()
        
        if v == end:
            return True
        
        if v != None and not v.discovered:
            v.discovered = True
            for edge in v.edges:
                Q.put(edge)
    
    return False
'''
if __name__ == '__main__':
    if len(argv) < 2:
        print("No Maze provided")
    else:
        m = maze(argv[1])
        DFS(m.graph, m.start, m.end)
        m.path = reconstruct(m.graph, m.end)
        m.setpath()
        if len(argv) > 2: m.save(argv[2])
        else: m.save()