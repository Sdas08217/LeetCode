# Minimum Bit Flips to Convert Number
class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        # XOR of start and goal gives us the differing bits
        xor_result = start ^ goal
        # Count the number of 1s in the XOR result, which corresponds to the number of flips
        return bin(xor_result).count('1')

# Example usage:
solution = Solution()
print(solution.minBitFlips(10, 7))  # Output: 3
print(solution.minBitFlips(3, 4))   # Output: 3
