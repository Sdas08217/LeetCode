# Fraction Addition and Subtraction
class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        from fractions import Fraction
        
        # Initialize result as a fraction
        result = Fraction(0, 1)
        i = 0
        n = len(expression)
        
        while i < n:
            # Read the sign
            sign = 1
            if expression[i] in '+-':
                if expression[i] == '-':
                    sign = -1
                i += 1
            
            # Read the numerator
            num_start = i
            while i < n and expression[i].isdigit():
                i += 1
            numerator = sign * int(expression[num_start:i])
            
            # Skip the '/' character
            i += 1
            
            # Read the denominator
            denom_start = i
            while i < n and expression[i].isdigit():
                i += 1
            denominator = int(expression[denom_start:i])
            
            # Add the fraction to the result
            result += Fraction(numerator, denominator)
        
        # Convert the result to the required format
        return "{}/{}".format(result.numerator, result.denominator)
# Example usage
solution = Solution()
print(solution.fractionAddition("-1/2+1/2"))  # Output: "0/1"
print(solution.fractionAddition("-1/2+1/2+1/3"))  # Output: "1/3"
print(solution.fractionAddition("1/3-1/2"))  # Output: "-1/6"
