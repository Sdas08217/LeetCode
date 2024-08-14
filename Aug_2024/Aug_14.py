# Find K-th Smallest Pair Distance
class Solution(object):
    def countPairs(self, nums, mid):
        count = 0
        j = 0
        for i in range(len(nums)):
            while j < len(nums) and nums[j] - nums[i] <= mid:
                j += 1
            count += j - i - 1
        return count

    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        
        while left < right:
            mid = (left + right) // 2
            if self.countPairs(nums, mid) < k:
                left = mid + 1
            else:
                right = mid
        
        return left

  # Example usage
solution = Solution()

# Example 1
nums1 = [1, 3, 1]
k1 = 1
result1 = solution.smallestDistancePair(nums1, k1)
print(f"Example 1: The {k1}th smallest distance in {nums1} is {result1}")

# Example 2
nums2 = [1, 1, 1]
k2 = 2
result2 = solution.smallestDistancePair(nums2, k2)
print(f"Example 2: The {k2}th smallest distance in {nums2} is {result2}")

# Example 3
nums3 = [1, 6, 1]
k3 = 3
result3 = solution.smallestDistancePair(nums3, k3)
print(f"Example 3: The {k3}th smallest distance in {nums3} is {result3}")
