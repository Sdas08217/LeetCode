from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Step 1: Find the maximum possible bitwise OR
        # The maximum possible bitwise OR of any subset is achieved by ORing all elements together.
        # This is because the OR operation can only set bits to 1, never unset them.
        max_or_value = 0
        for num in nums:
            max_or_value |= num
        
        # Initialize a counter for subsets that achieve the maximum bitwise OR
        count = 0
        
        # Step 2: Count subsets with the maximum bitwise OR using backtracking (Depth-First Search)
        # We'll explore all possible subsets recursively.
        def backtrack(index, current_or):
            nonlocal count  # Allows modification of the 'count' variable from the outer scope
            
            # Base case: If we have considered all elements in the 'nums' array
            if index == n:
                # If the bitwise OR of the current subset equals the maximum possible OR,
                # then we've found one such subset.
                if current_or == max_or_value:
                    count += 1
                return
            
            # Option 1: Exclude the current number (nums[index]) from the subset
            # Move to the next element without changing the current_or value.
            backtrack(index + 1, current_or)
            
            # Option 2: Include the current number (nums[index]) in the subset
            # Update current_or by performing a bitwise OR with nums[index], then move to the next element.
            backtrack(index + 1, current_or | nums[index])
            
        # Initial call to the backtracking function:
        # Start from the first element (index 0) with an initial bitwise OR value of 0
        # (representing an empty subset's OR value before elements are added).
        backtrack(0, 0)
        
        return count
