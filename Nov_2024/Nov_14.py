# Minimized Maximum of Products Distributed to Any Store
from typing import List
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def canDistribute(max_per_store):
            # Calculate the number of stores required if no store can have more than `max_per_store` products.
            required_stores = sum((quantity + max_per_store - 1) // max_per_store for quantity in quantities)
            return required_stores <= n
        
        # Binary search on the maximum number of products per store
        left, right = 1, max(quantities)
        while left < right:
            mid = (left + right) // 2
            if canDistribute(mid):
                right = mid  # Try for a smaller max
            else:
                left = mid + 1  # Increase the max to make it feasible
        
        return left

  
