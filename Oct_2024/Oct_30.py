# Minimum Number of Removals to Make Mountain Array
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        # Step 1: Compute LIS from the left
        left = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    left[i] = max(left[i], left[j] + 1)
        # Step 2: Compute LIS from the right
        right = [1] * n
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[j] < nums[i]:
                    right[i] = max(right[i], right[j] + 1)
        # Step 3: Find the longest mountain length
        longest_mountain = 0
        for i in range(1, n - 1):  # i cannot be the first or last element
            if left[i] > 1 and right[i] > 1:  # Valid mountain peak
                longest_mountain = max(longest_mountain, left[i] + right[i] - 1)
        # Step 4: Minimum removals to make it a mountain array
        return n - longest_mountain

# Example input
nums = [2, 1, 1, 5, 6, 2, 3, 1]

# Creating an instance of Solution and calling the method
solution = Solution()
result = solution.minimumMountainRemovals(nums)

# Output the result
print("Minimum removals to make a mountain array:", result)

  
