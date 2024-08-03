# Make Two Arrays Equal by Reversing Subarrays
from collections import Counter

class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        return Counter(target) == Counter(arr)

# Example usage
solution = Solution()

# Example 1
target1 = [1, 2, 3, 4]
arr1 = [2, 4, 1, 3]
print(solution.canBeEqual(target1, arr1))  # Output: True

# Example 2
target2 = [7]
arr2 = [7]
print(solution.canBeEqual(target2, arr2))  # Output: True

# Example 3
target3 = [3, 7, 9]
arr3 = [3, 7, 11]
print(solution.canBeEqual(target3, arr3))  # Output: False
