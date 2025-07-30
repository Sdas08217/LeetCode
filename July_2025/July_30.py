import math
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Step 1: Find the maximum element in the array.
        # This maximum element will be the 'k' discussed in the problem description.
        # Any bitwise AND of a subarray can be at most this maximum value.
        max_val = 0
        for num in nums:
            if num > max_val:
                max_val = num
        
        # Step 2: Find the length of the longest contiguous subarray
        # where all elements are equal to max_val.
        # If a subarray contains any element less than max_val, its bitwise AND
        # will be less than max_val. If it contains only max_val, its bitwise AND is max_val.
        
        max_length = 0
        current_length = 0
        
        for num in nums:
            if num == max_val:
                current_length += 1
            else:
                max_length = max(max_length, current_length)
                current_length = 0
        
        # After the loop, we need to check one last time, in case the longest
        # subarray of max_val ends at the end of the nums array.
        max_length = max(max_length, current_length)
        
        return max_length
