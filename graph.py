class graph:
    class vertex:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.prev = None
            self.edges = [None] * 4 #0:Left, 1:Right, 2:Up, 3:Down
    
    def __init__(self):
        self.vertices = []
    
    def addvertex(self, x, y):
        v = graph.vertex(x, y)
        self.vertices.append(v)
        return v

def reconstruct(G, v):
    path = [(v.x,v.y)]
    while v.prev != None:
        v = v.prev
        path.append((v.x,v.y))
    return path