# Minimum Number of Swaps to Make the String Balanced
class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Initialize balance and max imbalance
        balance = 0
        max_imbalance = 0
        
        # Traverse the string
        for char in s:
            if char == '[':
                balance += 1  # opening bracket reduces imbalance
            else:
                balance -= 1  # closing bracket increases imbalance
            # Track the maximum imbalance
            max_imbalance = min(max_imbalance, balance)
        
        # The minimum number of swaps is half the maximum imbalance
        return (-max_imbalance + 1) // 2  # integer division

# Example usage
s = "[]][]["
solution = Solution()
result = solution.minSwaps(s)
print(f"The minimum number of swaps required: {result}")
