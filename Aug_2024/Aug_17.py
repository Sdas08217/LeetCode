# Maximum Number of Points with Cost
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        m, n = len(points), len(points[0])
        dp = points[0]
        
        for r in range(1, m):
            left = [0] * n
            right = [0] * n
            
            # Fill the left array
            left[0] = dp[0]
            for c in range(1, n):
                left[c] = max(left[c - 1] - 1, dp[c])
            
            # Fill the right array
            right[n - 1] = dp[n - 1]
            for c in range(n - 2, -1, -1):
                right[c] = max(right[c + 1] - 1, dp[c])
            
            # Update dp for the current row
            for c in range(n):
                dp[c] = points[r][c] + max(left[c], right[c])
        
        return max(dp)
# Example usage
solution = Solution()

# Test case 1
points1 = [[1, 2, 3], [1, 5, 1], [3, 1, 1]]
print(solution.maxPoints(points1))  # Output: 9

# Test case 2
points2 = [[1, 5], [2, 3], [4, 2]]
print(solution.maxPoints(points2))  # Output: 11
