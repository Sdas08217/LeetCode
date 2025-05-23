from typing import List

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        total = sum(nums)
        gains = [(num ^ k) - num for num in nums]
        gains.sort(reverse=True)

        max_sum = total
        current_gain = 0

        for i in range(len(nums)):
            current_gain += gains[i]
            if (i + 1) % 2 == 0:
                max_sum = max(max_sum, total + current_gain)

        return max_sum
