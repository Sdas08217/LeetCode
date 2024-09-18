# Largest Number
from functools import cmp_to_key

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # Custom comparator function
        def compare(x, y):
            if x + y > y + x:
                return -1
            else:
                return 1

        # Convert integers to strings for easy concatenation
        nums = list(map(str, nums))

        # Sort with custom comparator
        nums.sort(key=cmp_to_key(compare))

        # Join the sorted numbers to form the largest number
        largest_num = ''.join(nums)

        # Edge case: If the largest number starts with '0', it means all were zeros
        if largest_num[0] == '0':
            return '0'

        return largest_num

# Example usage
nums1 = [10, 2]
nums2 = [3, 30, 34, 5, 9]

# Create an instance of the Solution class
sol = Solution()

# Call the largestNumber method with example inputs
result1 = sol.largestNumber(nums1)
result2 = sol.largestNumber(nums2)

# Print the results
print("Largest number for nums1:", result1)  # Output: "210"
print("Largest number for nums2:", result2)  # Output: "9534330"

