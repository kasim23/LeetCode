class AdjMatrixGraph:
    def __init__(self, vertices=None, edges=None):
        # Create an n x n matrix filled with zeros,
        # where n is the number of vertices.
        self.adj_matrix = [[0 for _ in range(len(vertices))] for _ in range(len(vertices))]
