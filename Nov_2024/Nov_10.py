# Shortest Subarray With OR at Least K II
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 1
        
        ans = len(nums) + 1
        bits = [0] * 32
        left = 0
        n = len(nums)
        for right in range(n):
            temp = 0
            for i in range(32):
                if nums[right] & (1 << i):
                    bits[i] += 1
                if bits[i] > 0:
                    temp |= (1 << i)
            
            if temp >= k:
                ans = min(ans, right - left + 1)
            
            while temp >= k:  # Constraints not satisfying, so move the left pointer
                temp = 0
                for i in range(32):
                    if nums[left] & (1 << i):
                        bits[i] -= 1
                    if bits[i] > 0:
                        temp |= (1 << i)
                
                left += 1
                if temp >= k:
                    ans = min(ans, right - left + 1)
        return -1 if ans == (len(nums) + 1) else ans

  # Example usage
solution = Solution()
nums = [1, 2, 4, 8, 16]
k = 7
result = solution.minimumSubarrayLength(nums, k)
print("Minimum subarray length:", result)
