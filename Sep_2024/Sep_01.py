# Convert 1D Array Into 2D Array
class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        # Check if reshaping is possible
        if len(original) != m * n:
            return []
        
        # Create the 2D array
        result = []
        for i in range(0, len(original), n):
            result.append(original[i:i + n])
        
        return result


# Example 1
solution = Solution()
original = [1, 2, 3, 4]
m = 2
n = 2
print(solution.construct2DArray(original, m, n))
# Output: [[1, 2], [3, 4]]

# Example 2
original = [1, 2, 3]
m = 1
n = 3
print(solution.construct2DArray(original, m, n))
# Output: [[1, 2, 3]]

# Example 3
original = [1, 2]
m = 1
n = 1
print(solution.construct2DArray(original, m, n))
# Output: []
