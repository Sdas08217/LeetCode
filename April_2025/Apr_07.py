class Solution:
    def canPartition(self, nums):
        total = sum(nums)
        
        # If the sum is odd, we can't split into two equal parts
        if total % 2 != 0:
            return False

        target = total // 2
        n = len(nums)
        
        # dp[i] will be True if a subset with sum i can be formed
        dp = [False] * (target + 1)
        dp[0] = True  # Base case: sum 0 is always possible

        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[target]
