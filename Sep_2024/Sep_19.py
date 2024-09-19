# Different Ways to Add Parentheses
class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        memo = {}
        
        def compute(expression):
            if expression in memo:
                return memo[expression]
            
            result = []
            for i, char in enumerate(expression):
                if char in "+-*":
                    left = compute(expression[:i])
                    right = compute(expression[i+1:])
                    
                    for l in left:
                        for r in right:
                            if char == '+':
                                result.append(l + r)
                            elif char == '-':
                                result.append(l - r)
                            elif char == '*':
                                result.append(l * r)
            
            if not result:
                result.append(int(expression))
            
            memo[expression] = result
            return result
        
        return compute(expression)

  # Example usage
expression = "2*3-4*5"
solution = Solution()
print(solution.diffWaysToCompute(expression))  # Expected output: [-34, -14, -10, -10, 10]
'''
# Saving the code to an attachment
with open('/mnt/data/diff_ways_to_compute.py', 'w') as file:
    file.write(code)
