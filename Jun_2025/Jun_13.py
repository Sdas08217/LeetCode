from typing import List

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        
        def canFormPairs(maxDiff):
            count = 0
            i = 1
            while i < len(nums):
                if nums[i] - nums[i - 1] <= maxDiff:
                    count += 1
                    i += 2  # Skip both indices in this pair
                else:
                    i += 1
            return count >= p

        left, right = 0, nums[-1] - nums[0]
        answer = right
        
        while left <= right:
            mid = (left + right) // 2
            if canFormPairs(mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return answer
