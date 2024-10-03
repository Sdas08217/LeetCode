# Make Sum Divisible by P
class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        total_sum = sum(nums)
        rem = total_sum % p
        
        # If the sum is already divisible by p, return 0 (no removal needed)
        if rem == 0:
            return 0
        
        prefix_sum = 0
        min_len = len(nums)
        mod_map = {0: -1}  # To handle cases where a valid subarray starts from index 0
        
        for i, num in enumerate(nums):
            prefix_sum = (prefix_sum + num) % p
            target_mod = (prefix_sum - rem) % p
            
            if target_mod in mod_map:
                min_len = min(min_len, i - mod_map[target_mod])
            
            mod_map[prefix_sum] = i
        
        return min_len if min_len != len(nums) else -1

  # Example usage of the Solution class
solution = Solution()

# Example 1
nums1 = [3, 1, 4, 2]
p1 = 6
result1 = solution.minSubarray(nums1, p1)
print(f"Example 1 Output: {result1}")  # Expected output: 1

# Example 2
nums2 = [6, 3, 5, 2]
p2 = 9
result2 = solution.minSubarray(nums2, p2)
print(f"Example 2 Output: {result2}")  # Expected output: 2

# Example 3
nums3 = [1, 2, 3]
p3 = 3
result3 = solution.minSubarray(nums3, p3)
print(f"Example 3 Output: {result3}")  # Expected output: 0
