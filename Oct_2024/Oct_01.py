#Check If Array Pairs Are Divisible by k
class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        # Create a remainder frequency array
        remainder_count = [0] * k
        
        # Count remainders
        for num in arr:
            remainder = num % k
            remainder_count[remainder] += 1
        
        # Check pairs for remainder 0
        if remainder_count[0] % 2 != 0:
            return False
        
        # Check pairs for other remainders
        for i in range(1, k // 2 + 1):
            if remainder_count[i] != remainder_count[k - i]:
                return False
        
        # Special case when k is even
        if k % 2 == 0 and remainder_count[k // 2] % 2 != 0:
            return False
        
        return True

  # Example usage
sol = Solution()

# Test case 1
arr1 = [1, 2, 3, 4, 5, 10, 6, 7, 8, 9]
k1 = 5
print(sol.canArrange(arr1, k1))  # Output: True

# Test case 2
arr2 = [1, 2, 3, 4, 5, 6]
k2 = 7
print(sol.canArrange(arr2, k2))  # Output: True

# Test case 3
arr3 = [1, 2, 3, 4, 5, 6]
k3 = 10
print(sol.canArrange(arr3, k3))  # Output: False
