# Smallest Range Covering Elements from K Lists
import heapq

class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        min_heap = []
        max_value = float('-inf')

        # Step 1: Initialize the heap with the first element of each list
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0], i, 0))
            max_value = max(max_value, nums[i][0])

        # Step 2: Initialize the smallest range
        smallest_range = [float('-inf'), float('inf')]

        while min_heap:
            min_value, list_idx, element_idx = heapq.heappop(min_heap)

            # Update the range if the current range is smaller
            if max_value - min_value < smallest_range[1] - smallest_range[0]:
                smallest_range = [min_value, max_value]

            # If the current list is exhausted, stop the process
            if element_idx + 1 == len(nums[list_idx]):
                break

            # Add the next element from the current list to the heap
            next_value = nums[list_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_value, list_idx, element_idx + 1))
            max_value = max(max_value, next_value)

        return smallest_range

  # Example usage
nums = [
    [4, 10, 15, 24, 26],
    [0, 9, 12, 20],
    [5, 18, 22, 30]
]

# Create an instance of the Solution class
solution = Solution()

# Call the smallestRange method
result = solution.smallestRange(nums)

# Print the result
print("Smallest range is:", result)
