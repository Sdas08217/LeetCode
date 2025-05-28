# Divisible and Non-divisible Sums Difference
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # Total sum of numbers from 1 to n
        total = n * (n + 1) // 2
        
        # Number of integers divisible by m
        k = n // m
        
        # Sum of integers divisible by m
        sum_divisible = m * k * (k + 1) // 2
        
        # Sum of integers not divisible by m
        sum_not_divisible = total - sum_divisible
        
        # Return the difference
        return sum_not_divisible - sum_divisible
