# Longest Subarray With Maximum Bitwise AND
class Solution:
    def longestSubarray(self, nums):
        max_val = max(nums)  # Step 1: Find the maximum value in the array
        longest = 0
        current_length = 0
        
        for num in nums:
            if num == max_val:
                current_length += 1  # Increment the length if the current element is max_val
                longest = max(longest, current_length)  # Update the longest subarray length
            else:
                current_length = 0  # Reset the current length if the element is not max_val
        
        return longest

# Example usage:
solution = Solution()
print(solution.longestSubarray([1, 2, 3, 3, 2, 2]))  # Output: 2
print(solution.longestSubarray([1, 2, 3, 4]))  # Output: 1
