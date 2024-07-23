# Sort Array by Increasing Frequency
from collections import Counter

class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Step 1: Count the frequency of each number
        frequency = Counter(nums)
        
        # Step 2: Sort based on frequency and value
        nums.sort(key=lambda x: (frequency[x], -x))
        
        return nums

# Example usage:
solution = Solution()
print(solution.frequencySort([1,1,2,2,2,3]))  # Output: [3, 1, 1, 2, 2, 2]
print(solution.frequencySort([2,3,1,3,2]))    # Output: [1, 3, 3, 2, 2]
print(solution.frequencySort([-1,1,-6,4,5,-6,1,4,1]))  # Output: [5, -1, 4, 4, -6, -6, 1, 1, 1]
