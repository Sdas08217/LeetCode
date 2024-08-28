# Count Sub Islands
class Solution(object):
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        def dfs(i, j):
            if i < 0 or i >= len(grid2) or j < 0 or j >= len(grid2[0]) or grid2[i][j] == 0:
                return True
            grid2[i][j] = 0  # Mark as visited
            is_sub_island = grid1[i][j] == 1
            is_sub_island &= dfs(i + 1, j)
            is_sub_island &= dfs(i - 1, j)
            is_sub_island &= dfs(i, j + 1)
            is_sub_island &= dfs(i, j - 1)
            return is_sub_island

        sub_islands_count = 0

        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1:
                    if dfs(i, j):
                        sub_islands_count += 1

        return sub_islands_count


# Example usage of the Solution class
if __name__ == "__main__":
    # Create an instance of the Solution class
    sol = Solution()

    # Define the input grids
    grid1 = [
        [1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [1, 1, 0, 1, 1]
    ]
    grid2 = [
        [1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1],
        [0, 1, 0, 0, 0],
        [1, 0, 1, 1, 0],
        [0, 1, 0, 1, 0]
    ]

    # Call the countSubIslands method
    result = sol.countSubIslands(grid1, grid2)

    # Print the result
    print("Number of sub-islands:", result)
