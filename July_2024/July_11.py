# Reverse Substrings Between Each Pair of Parentheses
class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for char in s:
            if char == ')':
                # Pop characters until the matching '('
                temp = []
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())
                # Pop the '(' from the stack
                if stack:
                    stack.pop()
                # Push the reversed substring back to the stack
                stack.extend(temp)
            else:
                # Push current character to the stack
                stack.append(char)
        
        # Join the characters in the stack to form the final string
        return ''.join(stack)
# Example usage:
solution = Solution()
print(solution.reverseParentheses("(abcd)"))          # Output: "dcba"
print(solution.reverseParentheses("(u(love)i)"))      # Output: "iloveu"
print(solution.reverseParentheses("(ed(et(oc))el)"))  # Output: "leetcode"
