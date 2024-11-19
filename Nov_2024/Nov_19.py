# Maximum Sum of Distinct Subarrays With Length K
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        current_sum = 0
        max_sum = 0
        unique_elements = set()
        for right in range(n):
            # If the current element is already in the set, shrink the window
            while nums[right] in unique_elements:
                unique_elements.remove(nums[left])
                current_sum -= nums[left]
                left += 1
            # Add the current element to the window
            unique_elements.add(nums[right])
            current_sum += nums[right]
            # If the window size exceeds k, shrink it
            if right - left + 1 > k:
                unique_elements.remove(nums[left])
                current_sum -= nums[left]
                left += 1
            # If the window size is exactly k, update the max sum
            if right - left + 1 == k:
                max_sum = max(max_sum, current_sum)
        return max_sum
