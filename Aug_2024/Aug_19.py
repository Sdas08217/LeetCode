# 2 Keys Keyboard
class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = i  # maximum i operations (1 by 1 pasting)
            for j in range(1, i):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + i // j)
        return dp[n]

# Example usage:
solution = Solution()
print(solution.minSteps(3))  # Output: 3
print(solution.minSteps(1))  # Output: 0
