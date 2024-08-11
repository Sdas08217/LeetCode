# Minimum Number of Days to Disconnect Island
class Solution(object):
    def minDays(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def is_connected(grid):
            m, n = len(grid), len(grid[0])
            visited = [[False]*n for _ in range(m)]
            
            def dfs(x, y):
                if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] == 0 or visited[x][y]:
                    return
                visited[x][y] = True
                dfs(x-1, y)
                dfs(x+1, y)
                dfs(x, y-1)
                dfs(x, y+1)
            
            islands = 0
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and not visited[i][j]:
                        if islands > 0:
                            return False
                        islands += 1
                        dfs(i, j)
            
            return islands == 1
        
        if not is_connected(grid):
            return 0
        
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if not is_connected(grid):
                        return 1
                    grid[i][j] = 1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    for x in range(m):
                        for y in range(n):
                            if grid[x][y] == 1:
                                grid[x][y] = 0
                                if not is_connected(grid):
                                    return 2
                                grid[x][y] = 1
                    grid[i][j] = 1
        
        return 2

  # Example usage of the Solution class
grid1 = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
grid2 = [[1,1]]

solution = Solution()
result1 = solution.minDays(grid1)
result2 = solution.minDays(grid2)

print("Minimum number of days to disconnect grid1:", result1)
print("Minimum number of days to disconnect grid2:", result2)
