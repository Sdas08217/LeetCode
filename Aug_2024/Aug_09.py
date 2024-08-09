# Magic Squares In Grid
class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def is_magic(i, j):
            s = set()
            # Check if all elements are distinct and in the range [1, 9]
            for x in range(3):
                for y in range(3):
                    if grid[i + x][j + y] < 1 or grid[i + x][j + y] > 9:
                        return False
                    s.add(grid[i + x][j + y])
            if len(s) != 9:
                return False
            
            # Check the magic square properties
            if (grid[i][j] + grid[i][j+1] + grid[i][j+2] != 15 or
                grid[i+1][j] + grid[i+1][j+1] + grid[i+1][j+2] != 15 or
                grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2] != 15 or
                grid[i][j] + grid[i+1][j] + grid[i+2][j] != 15 or
                grid[i][j+1] + grid[i+1][j+1] + grid[i+2][j+1] != 15 or
                grid[i][j+2] + grid[i+1][j+2] + grid[i+2][j+2] != 15 or
                grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] != 15 or
                grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] != 15):
                return False
            return True
        
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows - 2):
            for j in range(cols - 2):
                if grid[i + 1][j + 1] == 5 and is_magic(i, j):
                    count += 1
        return count

  # Example usage
grid = [[4, 3, 8, 4],
        [9, 5, 1, 9],
        [2, 7, 6, 2]]

solution = Solution()
result = solution.numMagicSquaresInside(grid)
print(result)  # Output: 1
