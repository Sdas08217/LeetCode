# Maximum XOR for Each Query
class Solution:
    def getMaximumXor(self, nums: list[int], maximumBit: int) -> list[int]:
        n = len(nums)
        xorr = nums[0]
        max_xor = (1 << maximumBit) - 1
        
        for i in range(1, n):
            xorr ^= nums[i]
        
        ans = []
        for i in range(n):
            ans.append(xorr ^ max_xor)
            xorr ^= nums[n - 1 - i]
        
        return ans

# Example usage
nums = [0, 1, 1, 3]
maximumBit = 2
solution = Solution()
result = solution.getMaximumXor(nums, maximumBit)
print(result)  # Output should show the maximum XOR values in the expected order
