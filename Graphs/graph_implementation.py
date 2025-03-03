from collections import deque
import unittest
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
    def __init__(self, vertices=None, edges=None):
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
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
    
    def add_edges(self, u, v, directed=False):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj_list[u].append(v)
    
    
    def dfs(self, vertex, visited=None, order=None):
        if visited is None:
            visited = set()
        if order is None:
            order = []
        visited.add(vertex)
        order.append(vertex)
        
        for neighbor in self.adj_list[vertex]:
            if neighbor not in visited:
                self.dfs(neighbor, visited, order)
        return order
                
    def dfs_iterative(self, vertex, visited=None):
        order = []
        if visited is None:
            visited = set()
        stack = [vertex]
        
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                order.append(current)
                for neighbor in self.adj_list[current]:
                    if neighbor not in visited:
                        stack.append(neighbor)
        return order
    
    def bfs(self, vertex, visited=None):
        order = []
        if visited is None:
            visited = set()
        q = deque([vertex])
        visited.add(vertex)
        
        while q:
            current = q.popleft()
            order.append(current)
            for neighbor in self.adj_list[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
        return order
                    
                    
class TestGraphTraversals(unittest.TestCase):
    def setUp(self):
        # Create a new graph and add vertices and directed edges.
        # (You can adjust directed/undirected according to your implementation.)
        self.graph = Graph()
        for vertex in ['A', 'B', 'C', 'D', 'E']:
            self.graph.add_vertex(vertex)
        # Define edges so that the graph structure is known.
        # Here, for example, A connects to B and C,
        # B connects to D, C connects to D, and D connects to E.
        self.graph.add_edges('A', 'B', directed=True)
        self.graph.add_edges('A', 'C', directed=True)
        self.graph.add_edges('B', 'D', directed=True)
        self.graph.add_edges('C', 'D', directed=True)
        self.graph.add_edges('D', 'E', directed=True)
    
    def test_dfs_recursive(self):
        # Call the recursive DFS starting from 'A'
        order = self.graph.dfs('A')
        # Verify that all nodes are visited
        self.assertEqual(set(order), {'A', 'B', 'C', 'D', 'E'})
        # Verify that the starting node is first in the order
        self.assertEqual(order[0], 'A')
    
    def test_dfs_iterative(self):
        # Call the iterative DFS starting from 'A'
        order = self.graph.dfs_iterative('A')
        self.assertEqual(set(order), {'A', 'B', 'C', 'D', 'E'})
        self.assertEqual(order[0], 'A')
    
    def test_bfs(self):
        # Call BFS starting from 'A'
        order = self.graph.bfs('A')
        # For BFS, the expected order (level order) should be exactly:
        expected_order = ['A', 'B', 'C', 'D', 'E']
        self.assertEqual(order, expected_order)

if __name__ == '__main__':
    unittest.main()