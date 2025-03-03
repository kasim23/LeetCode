class AdjMatrixGraph:
    def __init__(self, vertices=None, edges=None):
        # Create an n x n matrix filled with zeros,
        # where n is the number of vertices.
        self.adj_matrix = [[0 for _ in range(len(vertices))] for _ in range(len(vertices))]
        
        
        
    def add_vertex(self, vertex):
        pass
    
    
    def add_edge(self, u, v, directed=True):
        pass
    
    
    def remove_vertex(self, vertex):
        pass
    
    
    def remove_edge(self, u, v, directed=True):
        pass
    
    
    def has_edge(self, u, v):
        pass
    
    
    def get_neighbors(self, vertex):
        pass
    
    
    def __str__(self):
        pass
    
    
    def recursive_dfs(self, vertex, visited=None):
        pass
    
    
    def iterative_dfs(self, vertex, visited=None):
        pass
    
    
    def bfs(self, vertex, visited=None):
        pass
