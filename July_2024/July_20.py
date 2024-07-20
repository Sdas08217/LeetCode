# Find Valid Matrix Given Row and Column Sums
class Solution(object):
    def restoreMatrix(self, rowSum, colSum):
        """
        :type rowSum: List[int]
        :type colSum: List[int]
        :rtype: List[List[int]]
        """
        # Get the number of rows and columns
        num_rows = len(rowSum)
        num_cols = len(colSum)
        
        # Initialize the result matrix with zeros
        matrix = [[0] * num_cols for _ in range(num_rows)]
        
        # Iterate over the rows and columns
        for i in range(num_rows):
            for j in range(num_cols):
                # Determine the value for the cell (i, j)
                value = min(rowSum[i], colSum[j])
                matrix[i][j] = value
                
                # Update the row and column sums
                rowSum[i] -= value
                colSum[j] -= value
        
        return matrix

# Example usage:
sol = Solution()

# Example 1
rowSum1 = [3, 8]
colSum1 = [4, 7]
print(sol.restoreMatrix(rowSum1, colSum1))

# Example 2
rowSum2 = [5, 7, 10]
colSum2 = [8, 6, 8]
print(sol.restoreMatrix(rowSum2, colSum2))
