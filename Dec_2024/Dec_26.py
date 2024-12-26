class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        
        # Check if target is achievable
        if (total_sum + target) % 2 != 0 or total_sum < abs(target):
            return 0
        
        subset_sum = (total_sum + target) // 2
        
        # Initialize DP array
        dp = [0] * (subset_sum + 1)
        dp[0] = 1  # There's one way to make sum 0
        
        # Update DP array
        for num in nums:
            for j in range(subset_sum, num - 1, -1):
                dp[j] += dp[j - num]
        
        return dp[subset_sum]
