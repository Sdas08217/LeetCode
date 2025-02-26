from typing import List

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = 0  # Maximum subarray sum
        min_sum = 0  # Minimum subarray sum
        curr_max = 0 # Current maximum sum
        curr_min = 0 # Current minimum sum

        for num in nums:
            curr_max = max(num, curr_max + num)
            max_sum = max(max_sum, curr_max)

            curr_min = min(num, curr_min + num)
            min_sum = min(min_sum, curr_min)

        return max(abs(max_sum), abs(min_sum))

# Example usage:
solution = Solution()
print(solution.maxAbsoluteSum([1, -3, 2, 3, -4]))  # Output: 5
print(solution.maxAbsoluteSum([2, -5, 1, -4, 3, -2]))  # Output: 8
