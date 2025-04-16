from typing import List
from collections import defaultdict

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        count = 0
        left = 0
        freq = defaultdict(int)
        total_pairs = 0
        result = 0

        for right in range(len(nums)):
            # Count how many pairs this number adds
            total_pairs += freq[nums[right]]
            freq[nums[right]] += 1

            # Shrink the window from the left while we have enough pairs
            while total_pairs >= k:
                # This subarray [left, right] and all that start further right are good
                result += len(nums) - right
                total_pairs -= freq[nums[left]] - 1
                freq[nums[left]] -= 1
                left += 1

        return result
