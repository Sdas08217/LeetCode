# Stone Game II
class Solution:
    def stoneGameII(self, piles):
        n = len(piles)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        suffix_sum = [0] * (n + 1)

        # Compute the suffix sums
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        # Fill the dp table
        for i in range(n - 1, -1, -1):
            for M in range(1, n + 1):
                max_stones = 0
                for X in range(1, 2 * M + 1):
                    if i + X <= n:
                        max_stones = max(max_stones, suffix_sum[i] - dp[i + X][max(M, X)])
                dp[i][M] = max_stones

        return dp[0][1]

  # Create an instance of the Solution class
solution = Solution()

# Example 1
piles1 = [2, 7, 9, 4, 4]
result1 = solution.stoneGameII(piles1)
print(f"Maximum stones Alice can get (Example 1): {result1}")

# Example 2
piles2 = [1, 2, 3, 4, 5, 100]
result2 = solution.stoneGameII(piles2)
print(f"Maximum stones Alice can get (Example 2): {result2}")
