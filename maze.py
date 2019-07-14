from PIL import Image
from graph import *

class maze:
    def __init__(self, filename):
        self.filename = filename
        self.im = Image.open(filename)
        self.width = self.im.size[0]
        self.height = self.im.size[1]
        data = list(self.im.getdata(0))
        
        self.start = None
        self.end = None
        self.graph = graph()
        self.graph.path = []
        
        prevline = [None] * self.width
        curline = [None] * self.width
        
        for x in range(1, self.width - 1): #start row
            if data[x]:
                self.start = self.graph.addvertex(x, 0)
                prevline[x] = self.start
                break
        
        for y in range(1, self.height - 1):
            prev = None
            for x in range(1, self.width - 1):
                if data[y * self.width + x]:
                    cur = self.graph.addvertex(x, y)
                    curline[x] = cur
                    if prev != None:
                        cur.edges[0] = prev
                        prev.edges[1] = cur
                    
                    if prevline[x] != None:
                        cur.edges[2] = prevline[x]
                        prevline[x].edges[3] = cur
                    
                    prev = cur
                else:
                    prev = None
                
            prevline = curline
            curline = [None] * self.width
        
        for x in range(1, self.width - 1): #end row
            if data[(self.height - 1) * self.width + x]:
                self.end = self.graph.addvertex(x, self.height - 1)
                self.end.edges[2] = prevline[x]
                prevline[x].edges[3] = self.end
                break
    
    def save(self, filename = None):
        for c in self.path:
            self.im.putpixel(c, (255,0,0))
        if filename == None:
            self.im.save(self.filename[:-4] + "_new" + self.filename[-4:])
        else:
            self.im.save(filename)