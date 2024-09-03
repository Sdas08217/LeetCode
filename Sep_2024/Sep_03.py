# Sum of Digits of String After Convert
class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # Step 1: Convert the string to its corresponding integer string
        num_str = ''.join(str(ord(char) - ord('a') + 1) for char in s)
        
        # Convert to an integer for the first summing operation
        current_sum = sum(int(digit) for digit in num_str)
        
        # Step 2: Repeat the summing process k-1 times
        for _ in range(k - 1):
            current_sum = sum(int(digit) for digit in str(current_sum))
        
        return current_sum

#Example Usage
s1 = "iiii"
k1 = 1

s2 = "leetcode"
k2 = 2

s3 = "zbax"
k3 = 2

solution = Solution()
print(solution.getLucky(s1, k1))  # Output: 36
print(solution.getLucky(s2, k2))  # Output: 6
print(solution.getLucky(s3, k3))  # Output: 8
