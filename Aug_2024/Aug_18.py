# Ugly Number II
import heapq

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Initialize the min-heap and a set to keep track of seen numbers
        heap = [1]
        seen = {1}
        
        # Define the prime factors
        factors = [2, 3, 5]
        
        # The nth ugly number
        ugly_number = 1
        
        # Generate ugly numbers until we reach the nth one
        for _ in range(n):
            ugly_number = heapq.heappop(heap)
            for factor in factors:
                new_ugly = ugly_number * factor
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(heap, new_ugly)
        
        return ugly_number

  # Instantiate the Solution class
solution = Solution()

# Example 1
n1 = 10
result1 = solution.nthUglyNumber(n1)
print(f"The {n1}th ugly number is: {result1}")
# Output: The 10th ugly number is: 12

# Example 2
n2 = 1
result2 = solution.nthUglyNumber(n2)
print(f"The {n2}th ugly number is: {result2}")
# Output: The 1st ugly number is: 1

# Additional Example
n3 = 15
result3 = solution.nthUglyNumber(n3)
print(f"The {n3}th ugly number is: {result3}")
# Output: The 15th ugly number is: 24
Explanation:
Instantiate the Solution Class: solution = Solution() creates an instance of the Solution class.
Call the Method: solution.nthUglyNumber(n) is called with the desired value of n to find the nth ugly number.
Print the Result: The result is printed to verify the output.
This will give you the nth ugly number for different values of n as demonstrated.









