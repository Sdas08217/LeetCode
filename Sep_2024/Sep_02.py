# Find the Student that Will Replace the Chalk
class Solution(object):
    def chalkReplacer(self, chalk, k):
        """
        :type chalk: List[int]
        :type k: int
        :rtype: int
        """
        total_chalk = sum(chalk)
        k %= total_chalk  # Reduce k by the total chalk usage in one full round

        for i, chalk_needed in enumerate(chalk):
            if k < chalk_needed:
                return i
            k -= chalk_needed

      # Create an instance of the Solution class
solution = Solution()

# Example 1
chalk = [5, 1, 5]
k = 22
result = solution.chalkReplacer(chalk, k)
print(f"The student that will replace the chalk in Example 1 is student {result}.")  # Output: 0

# Example 2
chalk = [3, 4, 1, 2]
k = 25
result = solution.chalkReplacer(chalk, k)
print(f"The student that will replace the chalk in Example 2 is student {result}.")  # Output: 1


#Output

The student that will replace the chalk in Example 1 is student 0.
The student that will replace the chalk in Example 2 is student 1.
