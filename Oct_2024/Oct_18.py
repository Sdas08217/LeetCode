# Count Number of Maximum Bitwise-OR Subsets
class Solution:
    def countMaxOrSubsets(self, nums):
        # Step 1: Calculate the maximum possible bitwise OR of all elements
        max_or = 0
        for num in nums:
            max_or |= num
        
        # Step 2: Count the number of subsets with bitwise OR equal to max_or
        def subset_or(subset):
            result = 0
            for num in subset:
                result |= num
            return result
        
        n = len(nums)
        count = 0
        
        # Iterate over all possible non-empty subsets using combinations
        from itertools import combinations
        for r in range(1, n + 1):
            for subset in combinations(nums, r):
                if subset_or(subset) == max_or:
                    count += 1
                    
        return count

# Example usage of the Solution class
nums1 = [3, 1]
nums2 = [2, 2, 2]
nums3 = [3, 2, 1, 5]

solution = Solution()

# Call the function with different inputs
print(solution.countMaxOrSubsets(nums1))  # Output: 2
print(solution.countMaxOrSubsets(nums2))  # Output: 7
print(solution.countMaxOrSubsets(nums3))  # Output: 6

