from typing import List

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res = set()        # Stores all distinct OR results
        prev = set()       # Stores ORs of subarrays ending at previous index

        for num in arr:
            curr = {num}   # New set for subarrays ending at current index
            for p in prev:
                curr.add(p | num)  # Extend previous subarrays with current num
            res.update(curr)       # Add current ORs to result
            prev = curr            # Update prev for next iteration

        return len(res)
