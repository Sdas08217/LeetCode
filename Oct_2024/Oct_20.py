# Parsing A Boolean Expression
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        
        for char in expression:
            if char == ')':  # End of subexpression, evaluate it
                sub_expr = []
                
                # Pop until '(' and gather the subexpression elements
                while stack and stack[-1] != '(':
                    sub_expr.append(stack.pop())
                
                # Remove the '('
                stack.pop()
                
                # Get the operator before the '('
                operator = stack.pop()
                
                # Evaluate the subexpression based on the operator
                if operator == '!':
                    result = not (sub_expr[0] == 't')
                elif operator == '&':
                    result = all(x == 't' for x in sub_expr)
                elif operator == '|':
                    result = any(x == 't' for x in sub_expr)
                
                # Push the result back onto the stack
                stack.append('t' if result else 'f')
            
            elif char != ',':
                # Push other characters except for commas
                stack.append(char)
        
        # The final result is in the stack (either 't' or 'f')
        return stack[0] == 't'

  # Example usage:
solution = Solution()
print(solution.parseBoolExpr("&(|(f))"))  # Output: False
print(solution.parseBoolExpr("|(f,f,f,t)"))  # Output: True
print(solution.parseBoolExpr("!(&(f,t))"))  # Output: True
