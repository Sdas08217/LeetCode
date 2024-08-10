# Regions Cut By Slashes
class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        n = len(grid)
        parent = list(range(4 * n * n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent[find(x)] = find(y)
        
        for i in range(n):
            for j in range(n):
                index = 4 * (i * n + j)
                if grid[i][j] == '/':
                    union(index, index + 3)
                    union(index + 1, index + 2)
                elif grid[i][j] == '\\':
                    union(index, index + 1)
                    union(index + 2, index + 3)
                else:
                    union(index, index + 1)
                    union(index + 1, index + 2)
                    union(index + 2, index + 3)
                
                if i < n - 1:
                    union(index + 2, index + 4 * n)
                if j < n - 1:
                    union(index + 1, index + 7)
        
        return sum(parent[x] == x for x in range(4 * n * n))

  # Example Usage
grid = ["/\\", "\\/"]
solution = Solution()
result = solution.regionsBySlashes(grid)
print(result)  # Output: 5
