from typing import List

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        # Step 1: Sort the array to group close numbers together
        nums.sort()
        
        # Step 2: Initialize the count of subsequences and the starting element
        count = 1
        start = nums[0]
        
        # Step 3: Iterate through the sorted list
        for num in nums:
            # If the current number is too far from the start, start a new subsequence
            if num - start > k:
                count += 1
                start = num  # Reset start to the new group beginning
        
        # Step 4: Return the total number of subsequences needed
        return count
