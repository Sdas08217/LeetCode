# Maximum Width Ramp
class Solution:
    def maxWidthRamp(self, nums):
        stack = []
        max_width = 0
        
        # Step 1: Build a decreasing stack of indices
        for i in range(len(nums)):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
        
        # Step 2: Traverse from right to left and try to form the widest ramp
        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[j] >= nums[stack[-1]]:
                i = stack.pop()
                max_width = max(max_width, j - i)
        
        return max_width

#Example Usage 
# Create an instance of the Solution class
solution = Solution()

# Example input list
nums = [6, 0, 8, 2, 1, 5]

# Call the maxWidthRamp method and print the result
result = solution.maxWidthRamp(nums)
print("Maximum width of ramp:", result)
