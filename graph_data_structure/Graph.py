from _collections import defaultdict
from platform import node
class Graph:
    def __init__(self, size):
        self.size=size
        self.adjacency_matrix=[]
        for _ in range(size):
            self.adjacency_matrix.append([0 for _ in range(size)])
        self.vertices=size
        self.graph=defaultdict(list)
        
    def add_edge_using_matrix_representation(self, v1, v2):
        if v1==v2:
            print('vertexes are same')
        self.adjacency_matrix[v1][v2]=1
        self.adjacency_matrix[v2][v1]=1
        
    def add_edge_using_adjacency_list(self, v1, v2):
        self.graph[v1].append(v2)
        
    
    def to_string_using_matrix_representation(self):
        for row in self.adjacency_matrix:
            for val in row:
                print('{:4}'.format(val), end=''),
            print()
    
    def to_string_using_adjacency_list(self):
        for vertex, list in self.graph.items():
            print(vertex,' --> ', self.graph[vertex])
            
    def BFS(self, element):
        queue=[]
        visited=[]
        queue.append(element)
        visited.append(element)
        while queue:
            element=queue.pop(0)
            print(element, end=' ')
            for e in self.graph[element]:
                if e not in visited:
                    queue.append(e)
                    visited.append(e)
                    
        print()
                    
    def DFS(self, element):
        stack=[]
        stack.append(element)
        visited=[]
        while stack:
            element=stack.pop()
            print(element, end=' ')
            visited.append(element)
            for e in self.graph[element]:
                if e not in visited:
                    stack.append(e)
                    

g=Graph(5)
# g.add_edge_using_matrix_representation(0, 1);
# g.add_edge_using_matrix_representation(0, 2);
# g.add_edge_using_matrix_representation(1, 2);
# g.add_edge_using_matrix_representation(2, 0);
# g.add_edge_using_matrix_representation(2, 3);
# g.toString()
# g.add_edge_using_adjacency_list(2, 0)
# g.add_edge_using_adjacency_list(0, 1)
# g.add_edge_using_adjacency_list(0, 2)
# g.add_edge_using_adjacency_list(2, 3)
# g.add_edge_using_adjacency_list(1, 2)
# g.add_edge_using_adjacency_list(3, 3)

g.add_edge_using_adjacency_list(0, 1)
g.add_edge_using_adjacency_list(0, 2)
g.add_edge_using_adjacency_list(1, 3)
g.add_edge_using_adjacency_list(1, 4)
g.add_edge_using_adjacency_list(2, 4)
g.add_edge_using_adjacency_list(2, 5)
g.add_edge_using_adjacency_list(3, 6)
g.add_edge_using_adjacency_list(4, 6)
g.add_edge_using_adjacency_list(4, 7)
g.add_edge_using_adjacency_list(5, 7)
g.add_edge_using_adjacency_list(6, 8)
g.add_edge_using_adjacency_list(7, 8)
g.add_edge_using_adjacency_list(8, 8)
# g.to_string_using_adjacency_list()
g.BFS(0)
print('=================')
g.DFS(0)
# g.to_string_using_adjacency_list()

# g.to_string_using_adjacency_list()
# g.BFS(1)