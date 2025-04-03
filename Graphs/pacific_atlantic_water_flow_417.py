"""
    There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 

Example 1:
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
Example 2:

Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
 

Constraints:

m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 105

"""
from typing import List
from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
            using BFS starting from the ocean borders (one BFS for the Pacific and one for the Atlantic) and then taking the intersection of reachable cells is a very solid approach

Instead of asking, "Can water from cell X reach the ocean?" we ask, "Starting at the ocean, which cells can be reached by moving uphill or on flat ground?

        REVERSE THE PROBLEM TO FLOW FROM OCEAN TO CELLS

        """
        rows, cols = len(heights), len(heights[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def pacific_bfs():
            visited_pacific = set()
            q_pacific = deque()
            for i in range(rows):
                for j in range(cols):
                    if i == 0 or j == 0:
                        q_pacific.append((i, j))
                        visited_pacific.add((i,j))

            while q_pacific:
                i, j = q_pacific.popleft()
                for di, dj in directions:
                    new_i, new_j = i+di, j+dj
                    if 0 <= new_i < rows and 0 <= new_j < cols:
                        if (new_i, new_j) not in visited_pacific and heights[new_i][new_j] >= heights[i][j]:
                            q_pacific.append((new_i, new_j))
                            visited_pacific.add((new_i, new_j))

            return visited_pacific
                        

        def atlantic_bfs():
            visited_atlantic = set()
            q_atlantic = deque()
            for i in range(rows):
                for j in range(cols):
                    if i == rows - 1 or j == cols - 1:
                        q_atlantic.append((i, j))
                        visited_atlantic.add((i,j))

            while q_atlantic:
                i, j = q_atlantic.popleft()
                for di, dj in directions:
                    new_i, new_j = i+di, j+dj
                    if 0 <= new_i < rows and 0 <= new_j < cols:
                        if (new_i, new_j) not in visited_atlantic and heights[new_i][new_j] >= heights[i][j]:
                            q_atlantic.append((new_i, new_j))
                            visited_atlantic.add((new_i, new_j))
            
            return visited_atlantic

        visited_pacific = pacific_bfs()    # a set of coordinates reachable from the Pacific
        visited_atlantic = atlantic_bfs()    # a set of coordinates reachable from the Atlantic

        results = visited_pacific & visited_atlantic
        result_list = [list(coord) for coord in results]
        return result_list
