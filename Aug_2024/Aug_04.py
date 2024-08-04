# Range Sum of Sorted Subarray Sums
class Solution(object):
    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        # Step 1: Calculate all subarray sums
        subarray_sums = []
        for start in range(n):
            current_sum = 0
            for end in range(start, n):
                current_sum += nums[end]
                subarray_sums.append(current_sum)
        
        # Step 2: Sort the subarray sums
        subarray_sums.sort()
        
        # Step 3: Compute the sum from index left to right (1-based index)
        result = sum(subarray_sums[left-1:right]) % MOD
        
        # Step 4: Return the result modulo 10^9 + 7
        return result

# Example usage:
solution = Solution()
nums = [1, 2, 3, 4]
n = 4
left = 1
right = 5
print(solution.rangeSum(nums, n, left, right))  # Output: 13

left = 3
right = 4
print(solution.rangeSum(nums, n, left, right))  # Output: 6

left = 1
right = 10
print(solution.rangeSum(nums, n, left, right))  # Output: 50
