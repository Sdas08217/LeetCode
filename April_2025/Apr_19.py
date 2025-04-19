from typing import List
import bisect

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        count = 0
        n = len(nums)

        for i in range(n):
            left = bisect.bisect_left(nums, lower - nums[i], i + 1)
            right = bisect.bisect_right(nums, upper - nums[i], i + 1)
            count += (right - left)
        
        return count
