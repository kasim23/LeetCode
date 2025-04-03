"""
    You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

 

Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Explanation:
In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

Example 2:

Input: board = [["X"]]

Output: [["X"]]

 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.

"""
from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        
        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return
             # If the current cell is not an 'O', nothing to do.
            if board[i][j] != 'O':
                return

            # Mark the current cell as safe (temporary marker).
            board[i][j] = 'T'
             # Recursively call DFS for the four adjacent cells.
            dfs(i + 1, j)  # Down
            dfs(i - 1, j)  # Up
            dfs(i, j + 1)  # Right
            dfs(i, j - 1)  # Left
        
        # Check the top and bottom rows
        for j in range(cols):
            if board[0][j] == 'O':
        # Start DFS/BFS from (0, j)
                dfs(0, j)
            if board[rows - 1][j] == 'O':
        # Start DFS/BFS from (rows - 1, j)
                dfs(rows - 1, j)
                
        # Check the left and right columns
        for i in range(rows):
            if board[i][0] == 'O':
        # Start DFS/BFS from (i, 0)
                dfs(i, 0)
            if board[i][cols - 1] == 'O':
        # Start DFS/BFS from (i, cols - 1)
                dfs(i, cols - 1)


        # Post-processing: flip all remaining 'O's to 'X'
        # and revert the temporary marker 'T' back to 'O'.
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    # This 'O' was not reached by DFS, so it's surrounded.
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    # This 'O' was connected to the border, so revert it.
                    board[i][j] = 'O'
