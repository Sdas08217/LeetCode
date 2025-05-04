from collections import defaultdict
from typing import List

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = defaultdict(int)
        res = 0

        for a, b in dominoes:
            key = tuple(sorted((a, b)))  # Normalize domino: (1,2) and (2,1) become (1,2)
            res += count[key]            # Add how many times we've already seen this domino
            count[key] += 1              # Increment the count

        return res
