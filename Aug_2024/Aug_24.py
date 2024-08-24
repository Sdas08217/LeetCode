# Find the Closest Palindrome

class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        length = len(n)
        candidates = set()
        
        # Edge case: 10..01, 9..9
        candidates.add(str(10**(length - 1) - 1))
        candidates.add(str(10**length + 1))
        
        # Get the first half of the number
        prefix = int(n[:(length + 1) // 2])
        
        # Generate palindromes based on the prefix
        for i in range(-1, 2):
            new_prefix = str(prefix + i)
            if length % 2 == 0:
                candidate = new_prefix + new_prefix[::-1]
            else:
                candidate = new_prefix + new_prefix[-2::-1]
            candidates.add(candidate)
        
        candidates.discard(n)  # Remove the number itself from candidates
        
        # Find the closest palindrome
        closest_palindrome = min(candidates, key=lambda x: (abs(int(x) - int(n)), int(x)))
        
        return closest_palindrome


# Create an instance of the Solution class
solution = Solution()

# Example 1
n1 = "123"
result1 = solution.nearestPalindromic(n1)
print(f"The closest palindrome to {n1} is {result1}.")  # Output: "121"

# Example 2
n2 = "1"
result2 = solution.nearestPalindromic(n2)
print(f"The closest palindrome to {n2} is {result2}.")  # Output: "0"
