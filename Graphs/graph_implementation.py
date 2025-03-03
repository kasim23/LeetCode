class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

#     def __str__(self):
#         return f'Node({self.value})'
    
#     def display(self):
#         connections = [node.value for node in self.neighbors]
#         return f'{self.value} is connected to: {connections}'


class Graph:
    def __init__(self, vertices, edges):
        # initialize adjacency list
        self.adj_list = {}
        # add vertices if provided
        if vertices:
            for vertex in vertices:
                self.add_vertex(vertex)
        # add edges if provided
        if edges:
            for u, v in edges:
                self.add_edge(u, v)
                
    def add_vertex(self, vertex):
        pass
    
    def add_edges(self, u, v, directed=False):
        pass