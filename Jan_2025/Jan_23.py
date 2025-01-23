from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # Get dimensions of the grid
        m, n = len(grid), len(grid[0])
        
        # Arrays to store the count of servers in each row and column
        row_count = [0] * m
        col_count = [0] * n
        
        # First pass: Count servers in each row and column
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1
        
        # Second pass: Count servers that can communicate
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (row_count[i] > 1 or col_count[j] > 1):
                    result += 1
        
        return result
