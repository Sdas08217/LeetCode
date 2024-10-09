# Minimum Add to Make Parentheses Valid
class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        open_needed = 0
        close_needed = 0
        
        for char in s:
            if char == '(':
                close_needed += 1
            elif char == ')':
                if close_needed > 0:
                    close_needed -= 1
                else:
                    open_needed += 1
        
        return open_needed + close_needed

  # Example usage
solution = Solution()
s1 = "())"
print(solution.minAddToMakeValid(s1))  # Output: 1

s2 = "((("
print(solution.minAddToMakeValid(s2))  # Output: 3
