# Rotate String
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Check if lengths are equal and if goal is a substring of s + s
        return len(s) == len(goal) and goal in (s + s)

  #Eaxmple Usage
  # Create an instance of the Solution class
solution = Solution()

# Define input strings
s = "abcde"
goal = "cdeab"

# Call the rotateString method and print the result
print(solution.rotateString(s, goal))  # Output: True
