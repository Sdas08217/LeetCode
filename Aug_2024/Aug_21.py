# Strange Printer 
class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 1  # A single character needs one turn
        
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = dp[i][j-1] + 1
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j])
                if s[i] == s[j]:
                    dp[i][j] = min(dp[i][j], dp[i][j-1])
        
        return dp[0][n-1]
# Example usage:
s = "aaabbb"
sol = Solution()
print(sol.strangePrinter(s))  # Output: 2
