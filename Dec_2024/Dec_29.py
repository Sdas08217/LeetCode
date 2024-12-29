class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        n = len(words[0])
        m = len(target)
        
        # Precompute the frequency of each character at each position in words
        char_count = [collections.Counter([word[i] for word in words]) for i in range(n)]
        
        # DP table: dp[j] represents the number of ways to form target[:j]
        dp = [0] * (m + 1)
        dp[0] = 1  # There's 1 way to form an empty target
        for i in range(n):  # Iterate over positions in words
            # Update dp table from back to front to avoid overwriting
            for j in range(m, 0, -1):  # Iterate over target indices
                if target[j - 1] in char_count[i]:
                    dp[j] += dp[j - 1] * char_count[i][target[j - 1]]
                    dp[j] %= MOD
        return dp[m]
