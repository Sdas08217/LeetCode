#Count Subarrays With Fixed Bounds
class Solution:
    def countSubarrays(self, nums, minK, maxK):
        res = 0
        last_min = last_max = last_invalid = -1
        
        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                last_invalid = i
            if num == minK:
                last_min = i
            if num == maxK:
                last_max = i
            res += max(0, min(last_min, last_max) - last_invalid)
        
        return res
