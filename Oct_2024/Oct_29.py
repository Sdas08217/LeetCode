# Maximum Number of Moves in a Grid
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = [[-1] * n for _ in range(m)]  # Initialize memo table with -1
        def dfs(i, j):
            # If we've already computed the result for this cell, return it
            if memo[i][j] != -1:
                return memo[i][j]
            max_moves = 0  # Initialize max moves from this cell
            # Explore the three possible directions
            for di, dj in [(-1, 1), (0, 1), (1, 1)]:
                ni, nj = i + di, j + dj  # New row and column
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] > grid[i][j]:
                    max_moves = max(max_moves, 1 + dfs(ni, nj))
            memo[i][j] = max_moves  # Store the result in memo
            return max_moves
        # Start DFS from every cell in the first column and find the max result
        max_result = 0
        for i in range(m):
            max_result = max(max_result, dfs(i, 0))
        return max_result

  # Example usage
from typing import List

# Initialize an instance of the Solution class
solution = Solution()

# Define the grid for which we want to calculate max moves
grid = [
    [3, 4, 5],
    [3, 2, 6],
    [2, 2, 1]
]

# Call the maxMoves function and print the result
result = solution.maxMoves(grid)
print("Maximum moves:", result)
