from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        i = 0

        while i < n:
            if i + 2 >= n:
                return []  # Not enough elements left to form a group

            group = nums[i:i+3]

            if group[2] - group[0] <= k:
                res.append(group)
                i += 3
            else:
                return []  # Cannot form a valid group, condition fails

        return res
