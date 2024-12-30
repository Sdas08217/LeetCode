class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7
        
        # dp[i] will store the number of good strings of length i
        dp = [0] * (high + 1)
        dp[0] = 1  # Base case: One way to create an empty string
        
        # Fill the dp array for lengths from 1 to high
        for length in range(1, high + 1):
            if length >= zero:
                dp[length] += dp[length - zero]
            if length >= one:
                dp[length] += dp[length - one]
            dp[length] %= MOD
        
        # Sum up all good strings of length in the range [low, high]
        return sum(dp[low:high + 1]) % MOD
# Example usage:
solution = Solution()
print(solution.countGoodStrings(3, 3, 1, 1))  # Output: 8
print(solution.countGoodStrings(2, 3, 1, 2))  # Output: 5
