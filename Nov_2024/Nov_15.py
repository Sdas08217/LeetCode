# Shortest Subarray to be Removed to Make Array Sorted.
from typing import List
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        
        # Step 1: Find the longest non-decreasing prefix
        left = 0
        while left < n - 1 and arr[left] <= arr[left + 1]:
            left += 1
        if left == n - 1:  # The whole array is already sorted
            return 0
        
        # Step 2: Find the longest non-decreasing suffix
        right = n - 1
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1
        
        # Step 3: Calculate minimum subarray removal
        result = min(n - left - 1, right)  # Option to remove all from left or all from right
        # Step 4: Try to combine left part and right part
        i, j = 0, right
        while i <= left and j < n:
            if arr[i] <= arr[j]:  # Valid connection
                result = min(result, j - i - 1)
                i += 1
            else:
                j += 1
        
        return result


# Example usage
if __name__ == "__main__":
    arr = [1, 2, 3, 10, 4, 2, 3, 5]
    solution = Solution()
    result = solution.findLengthOfShortestSubarray(arr)
    print(f"The length of the shortest subarray to remove is: {result}")
