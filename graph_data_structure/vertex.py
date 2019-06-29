import sys

class Vertex:
    def __init__(self, name):
        self.name=name
        self.visited=False
        self.adjacenciesList=[]
        self.predecessor=None
        self.minDistance=sys.maxsize        
    
    
    def __cmp__(self,other):
        return self.cmp(self.minDistance,other.minDistance)
    
    def __lt__(self,other):
        return self.minDistance<other.minDistance