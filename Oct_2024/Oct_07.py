# Minimum String Length After Removing Substrings
class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        
        for char in s:
            # Check if the last two characters form "AB" or "CD"
            if stack and ((stack[-1] == 'A' and char == 'B') or (stack[-1] == 'C' and char == 'D')):
                stack.pop()  # Remove the last character from the stack as "AB" or "CD" was found
            else:
                stack.append(char)  # Otherwise, add the character to the stack
        
        # The remaining characters in the stack form the minimized string
        return len(stack)
# Example usage
s = "ABFCACDB"
solution = Solution()
result = solution.minLength(s)
print("The minimized string length is:", result)
