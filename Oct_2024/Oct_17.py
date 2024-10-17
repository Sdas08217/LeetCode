# Maximum Swap
class Solution:
    def maximumSwap(self, num: int) -> int:
        # Convert number to a list of digits
        digits = list(str(num))
        n = len(digits)
        
        # Create a dictionary to store the last occurrence of each digit
        last_occurrence = {int(digits[i]): i for i in range(n)}
        
        # Traverse the digits
        for i in range(n):
            # Check if there is any larger digit later in the list
            for d in range(9, int(digits[i]), -1):
                if last_occurrence.get(d, -1) > i:
                    # Swap the current digit with the largest possible one
                    digits[i], digits[last_occurrence[d]] = digits[last_occurrence[d]], digits[i]
                    # Return the result as an integer
                    return int("".join(digits))
        
        # If no swap improves the number, return the original number
        return num

  #Example Usage
  # Create an instance of the Solution class
solution = Solution()

# Example 1: num = 2736
num1 = 2736
result1 = solution.maximumSwap(num1)
print(f"Maximum number after at most one swap for {num1}: {result1}")

# Example 2: num = 9973
num2 = 9973
result2 = solution.maximumSwap(num2)
print(f"Maximum number after at most one swap for {num2}: {result2}")
