# Minimum Array End
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        result = x
        remaining = n - 1
        position = 1
    
        while remaining:
            if not (x & position):
                result |= (remaining & 1) * position
                remaining >>= 1
            position <<= 1
    
        return result
# Create an instance of the Solution class
solution = Solution()

# Example 1
n = 5
x = 3
print(solution.minEnd(n, x))  # Outputs the result of minEnd with n = 5, x = 3

# Example 2
n = 10
x = 12
print(solution.minEnd(n, x))  # Outputs the result of minEnd with n = 10, x = 12
  
