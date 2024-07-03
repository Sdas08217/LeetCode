# Minimum Difference Between Largest and Smallest Value in Three Moves
class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 4:
            return 0
        
        nums.sort()
        n = len(nums)
        
        # Possible differences after making up to 3 changes
        return min(nums[n-1] - nums[3],  # Change the three smallest elements
                   nums[n-2] - nums[2],  # Change the two smallest and one largest element
                   nums[n-3] - nums[1],  # Change the one smallest and two largest elements
                   nums[n-4] - nums[0])  # Change the three largest elements

# Test cases
sol = Solution()
print(sol.minDifference([5, 3, 2, 4]))      # Output: 0
print(sol.minDifference([1, 5, 0, 10, 14])) # Output: 1
print(sol.minDifference([3, 100, 20]))      # Output: 0
