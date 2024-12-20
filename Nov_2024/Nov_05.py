# Minimum Number of Changes to Make Binary String Beautiful
class Solution:
    def minChanges(self, s: str) -> int:
        changes = 0
        
        # Loop through the string in steps of 2 to examine each pair
        for i in range(0, len(s), 2):
            # Check if the two characters in the current pair are different
            if s[i] != s[i + 1]:
                # Increment the change count if they are different
                changes += 1
                
        return changes

  # Example usage:
sol = Solution()
s = "010101"
print(sol.minChanges(s))  # Output will depend on the input string