from typing import List

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        prefix_sum = 0
        min_prefix = 0
        max_prefix = 0
        
        for diff in differences:
            prefix_sum += diff
            min_prefix = min(min_prefix, prefix_sum)
            max_prefix = max(max_prefix, prefix_sum)
        
        min_start = lower - min_prefix
        max_start = upper - max_prefix
        
        return max(0, max_start - min_start + 1)
