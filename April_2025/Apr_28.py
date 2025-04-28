# Count Subarrays With Score Less Than K
from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        total_sum = 0
        ans = 0

        for right in range(n):
            total_sum += nums[right]

            # Shrink window from the left if score is too big
            while total_sum * (right - left + 1) >= k:
                total_sum -= nums[left]
                left += 1

            # Count valid subarrays ending at 'right'
            ans += (right - left + 1)

        return ans
