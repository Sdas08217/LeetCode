# Count Subarrays Where Max Element Appears at Least K Times
from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_val = max(nums)
        count = 0
        left = 0
        max_count = 0

        for right in range(len(nums)):
            if nums[right] == max_val:
                max_count += 1

            while max_count >= k:
                # All subarrays starting from 'left' to end that include current 'right' are valid
                count += len(nums) - right
                if nums[left] == max_val:
                    max_count -= 1
                left += 1

        return count
