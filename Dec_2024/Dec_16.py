class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            min_index = nums.index(min(nums))  # Find the index of the first occurrence of the minimum value
            nums[min_index] *= multiplier  # Multiply the minimum value by the multiplier
        return nums
# Example usage
solution = Solution()
print(solution.getFinalState([2, 1, 3, 5, 6], 5, 2))  # Output: [8, 4, 6, 5, 6]
print(solution.getFinalState([1, 2], 3, 4))  # Output: [16, 8]
