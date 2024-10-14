# Maximal Score After Applying K Operations
import heapq
import math

class Solution(object):
    def maxKelements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Max-heap simulation using negative values
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        
        score = 0
        
        for _ in range(k):
            # Extract max element (negating since heap is a min-heap)
            max_element = -heapq.heappop(max_heap)
            score += max_element
            
            # Calculate the ceiling of max_element / 3
            next_value = (max_element + 2) // 3
            
            # Push the next value back into the heap (negated for max-heap)
            heapq.heappush(max_heap, -next_value)
        
        return score
#Eaxmple Usage
# Create an instance of the Solution class
solution = Solution()

# Test Case 1
nums1 = [10, 10, 10, 10, 10]
k1 = 5
result1 = solution.maxKelements(nums1, k1)
print("Test Case 1 Result:", result1)  # Output: 50

# Test Case 2
nums2 = [1, 10, 3, 3, 3]
k2 = 3
result2 = solution.maxKelements(nums2, k2)
print("Test Case 2 Result:", result2)  # Output: 17
