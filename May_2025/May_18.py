MOD = 10**9 + 7

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        # Generate all valid column patterns for given m
        def generate_patterns(m):
            from itertools import product
            colors = [0, 1, 2]  # 0: Red, 1: Green, 2: Blue
            patterns = []
            for pattern in product(colors, repeat=m):
                if all(pattern[i] != pattern[i+1] for i in range(m - 1)):
                    patterns.append(pattern)
            return patterns

        # Check if two patterns can be adjacent
        def is_valid_transition(p1, p2):
            return all(p1[i] != p2[i] for i in range(len(p1)))

        patterns = generate_patterns(m)
        num_patterns = len(patterns)
        # Initialize dp table
        dp = [[0] * num_patterns for _ in range(n)]
        for j in range(num_patterns):
            dp[0][j] = 1  # All patterns are valid for the first column

        # Fill the dp table
        for col in range(1, n):
            for j in range(num_patterns):
                for k in range(num_patterns):
                    if is_valid_transition(patterns[j], patterns[k]):
                        dp[col][j] = (dp[col][j] + dp[col - 1][k]) % MOD

        # Sum up all valid patterns for the last column
        return sum(dp[n - 1]) % MOD
