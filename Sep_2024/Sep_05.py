# Find Missing Observations
class Solution(object):
    def missingRolls(self, rolls, mean, n):
        """
        :type rolls: List[int]
        :type mean: int
        :type n: int
        :rtype: List[int]
        """
        m = len(rolls)
        total_sum = mean * (n + m)
        current_sum = sum(rolls)
        
        missing_sum = total_sum - current_sum
        
        # Check if the missing sum is within the valid range
        if missing_sum < n or missing_sum > 6 * n:
            return []
        
        # Distribute the missing sum over n rolls
        base_value = missing_sum // n
        remainder = missing_sum % n
        
        # Create the result array
        result = [base_value] * n
        
        # Distribute the remainder (increase some of the base values by 1)
        for i in range(remainder):
            result[i] += 1
        
        return result

  #Example Usage
# Create an instance of the Solution class
sol = Solution()

# Example 1
rolls = [3, 2, 4, 3]
mean = 4
n = 2
print(sol.missingRolls(rolls, mean, n))  # Output: [6, 6]

# Example 2
rolls = [1, 5, 6]
mean = 3
n = 4
print(sol.missingRolls(rolls, mean, n))  # Output: [2, 3, 2, 2]

# Example 3
rolls = [1, 2, 3, 4]
mean = 6
n = 4
print(sol.missingRolls(rolls, mean, n))  # Output: []
