# Minimum Swaps to Group All 1's Together II
class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total_ones = sum(nums)

        # Duplicate the array for circular behavior
        nums = nums + nums

        # Sliding window to find max number of 1s in any window of size `total_ones`
        max_ones_in_window = 0
        current_ones_in_window = 0

        # Initialize the first window
        for i in range(total_ones):
            if nums[i] == 1:
                current_ones_in_window += 1

        max_ones_in_window = current_ones_in_window

        # Slide the window
        for i in range(1, n):
            if nums[i - 1] == 1:
                current_ones_in_window -= 1
            if nums[i + total_ones - 1] == 1:
                current_ones_in_window += 1

            max_ones_in_window = max(max_ones_in_window, current_ones_in_window)

        # The minimum swaps needed is the difference between total_ones and max_ones_in_window
        min_swaps_needed = total_ones - max_ones_in_window
        return min_swaps_needed

# Example usage
solution = Solution()
print(solution.minSwaps([0, 1, 0, 1, 1, 0, 0]))  # Output: 1
print(solution.minSwaps([0, 1, 1, 1, 0, 0, 1, 1, 0]))  # Output: 2
print(solution.minSwaps([1, 1, 0, 0, 1]))  # Output: 0
