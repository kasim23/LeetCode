"""
    You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.

"""
from typing import List
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        q = deque()
        fresh_count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh_count += 1
        
        if fresh_count == 0:
            return 0

        minutes = 0

        while q:
            level_size = len(q)
            for _ in range(level_size):
                i, j = q.popleft()
                for di, dj in directions:
                    new_i, new_j = i + di, j + dj
                    if 0 <= new_i < rows and 0 <= new_j < cols and grid[new_i][new_j] == 1:
                        grid[new_i][new_j] = 2
                        fresh_count -= 1
                        q.append((new_i, new_j))

            if q:
                minutes += 1
        return minutes if fresh_count == 0 else -1
    
s = Solution()
grid1 = [[2,1,1],[1,1,0],[0,1,1]] # should be 4
grid2 = [[2,1,1],[0,1,1],[1,0,1]] # should be -1
grid3 = [[0,2]] # should be 0

print(s.orangesRotting(grid1)) # as expected, output is 4
print(s.orangesRotting(grid2)) # as expected, output is -1
print(s.orangesRotting(grid3)) # as expected, output is 0