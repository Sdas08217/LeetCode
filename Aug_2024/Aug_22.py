# Number Complement
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Find the number of bits in the binary representation of num
        bit_length = num.bit_length()
        
        # Create a mask with the same length as num but with all bits set to 1
        mask = (1 << bit_length) - 1
        
        # XOR num with the mask to get the complement
        return num ^ mask

  # Example usage:
solution = Solution()
print(solution.findComplement(5))  # Output: 2
print(solution.findComplement(1))  # Output: 0
