from sys import argv
from maze import *

def TurnLeft(G, start, end):
    dir = 2
    cur = start
    while cur != end:
        print(cur.x,cur.y,dir)
        numedges = 4-cur.edges.count(None)
        if numedges == 1:
            dir = back(dir)
            cur.prev = cur
            prev = cur
            cur = cur.edges[dir]
        elif numedges == 2:
            for i, edge in enumerate(cur.edges):
                if edge != prev and edge != None:
                    prev = cur
                    cur = edge
                    cur.prev = prev
                    dir = i
                    break
        else:
            cur.prev = prev
            prev = cur
            dir = left(dir)
            if cur.edges[dir]:
                cur = cur.edges[dir]
            else: 
                dir = right(dir)
                cur = cur.edges[dir]
    
    print(end.prev)

def back(dir):
    return dir + 2 if dir < 1 else dir - 2

def left(dir):
    return dir + 1 if dir < 3 else 0

def right(dir):
    return dir - 1 if dir > 0 else 3

if __name__ == '__main__':
    if len(argv) < 2:
        print("No Maze provided")
    else:
        m = maze(argv[1])
        TurnLeft(m.graph, m.start, m.end)
        m.path = reconstruct(m.graph, m.end)
        m.setpath()
        if len(argv) > 2: m.save(argv[2])
        else: m.save()