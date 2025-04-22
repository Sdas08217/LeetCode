MOD = 10**9 + 7

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        from math import log2
        
        # max depth of divisor chain = log2(maxValue)
        max_len = int(log2(maxValue)) + 1
        
        # dp[i][j] = number of sequences of length j ending with value i
        dp = [[0] * (max_len + 1) for _ in range(maxValue + 1)]

        # Base case: sequences of length 1
        for i in range(1, maxValue + 1):
            dp[i][1] = 1

        for length in range(1, max_len):
            for val in range(1, maxValue + 1):
                if dp[val][length] == 0:
                    continue
                for multiple in range(val * 2, maxValue + 1, val):
                    dp[multiple][length + 1] += dp[val][length]
                    dp[multiple][length + 1] %= MOD

        # Precompute factorials and inverse factorials for combinations
        factorial = [1] * (n + 1)
        for i in range(1, n + 1):
            factorial[i] = factorial[i - 1] * i % MOD

        inv_factorial = [1] * (n + 1)
        inv_factorial[n] = pow(factorial[n], MOD - 2, MOD)
        for i in range(n - 1, -1, -1):
            inv_factorial[i] = inv_factorial[i + 1] * (i + 1) % MOD

        def nCr(a, b):
            if b > a or b < 0:
                return 0
            return factorial[a] * inv_factorial[b] % MOD * inv_factorial[a - b] % MOD

        # Calculate the total number of ideal arrays
        total = 0
        for val in range(1, maxValue + 1):
            for length in range(1, max_len + 1):
                if dp[val][length]:
                    total += dp[val][length] * nCr(n - 1, length - 1)
                    total %= MOD

        return total
