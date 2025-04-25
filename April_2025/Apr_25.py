# Count of Interesting Subarrays
from collections import defaultdict
from typing import List

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        prefix_count = 0
        freq = defaultdict(int)
        freq[0] = 1  # Base case: zero prefix matches
        result = 0

        for num in nums:
            # Increment prefix count if current number satisfies condition
            if num % modulo == k:
                prefix_count += 1

            # Find number of previous prefix_counts that satisfy the condition
            target = (prefix_count - k + modulo) % modulo
            result += freq[target]

            # Update frequency map with current prefix count modulo
            freq[prefix_count % modulo] += 1

        return result
