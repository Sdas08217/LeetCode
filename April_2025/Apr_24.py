# Count Complete Subarrays in an Array
from typing import List

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        totalDistinct = len(set(nums))  # Count of all distinct elements in the array
        n = len(nums)
        count = 0

        for i in range(n):
            seen = set()
            for j in range(i, n):
                seen.add(nums[j])
                if len(seen) == totalDistinct:
                    count += 1
        return count
