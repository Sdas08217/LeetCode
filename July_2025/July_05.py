from typing import List
from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)  # Count frequency of each number
        lucky_numbers = [num for num, count in freq.items() if num == count]
        return max(lucky_numbers) if lucky_numbers else -1
