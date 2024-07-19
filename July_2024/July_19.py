# Lucky Numbers in a Matrix
class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # Find the minimum element in each row
        min_in_rows = [min(row) for row in matrix]
        
        # Find the maximum element in each column
        max_in_cols = [max(col) for col in zip(*matrix)]
        
        # Find all lucky numbers
        lucky_nums = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == min_in_rows[i] and matrix[i][j] == max_in_cols[j]:
                    lucky_nums.append(matrix[i][j])
        
        return lucky_nums


# Example usage:
matrix1 = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]
matrix2 = [[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]
matrix3 = [[7, 8], [1, 2]]

sol = Solution()
print(sol.luckyNumbers(matrix1)) # Output: [15]
print(sol.luckyNumbers(matrix2)) # Output: [12]
print(sol.luckyNumbers(matrix3)) # Output: [7]
