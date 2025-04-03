"""
    Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.


Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.

"""
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rows, cols = len(grid), len(grid[0])
        num_islands = 0
        
        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return 
            if grid[i][j] != "1" or (i, j) in visited:
                return
            
            visited.add((i,j))
            # explore neighbors (up, down, left, right)
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
            
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visited:
                    num_islands += 1
                    dfs(i,j)
                    
        return num_islands
    
# Test Case 1: Should return 1
island1 = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
# Test Case 2: Should return 3
island2 = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
s = Solution()
print(s.numIslands(island1)) # As expected returns 1
print(s.numIslands(island2)) # As expected returns 3