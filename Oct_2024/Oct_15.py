# Separate Black and White Balls
class Solution:
    def minimumSteps(self, s):
        swap, black = 0, 0
        for c in s:
            if c == "0":
                swap += black
            else:
                black += 1
        return swap

  # Create an instance of the Solution class
solution = Solution()

# Example input
s = "101"

# Call the minimumSteps method and print the result
result = solution.minimumSteps(s)
print(f"Minimum steps to move all '0's to the left: {result}")
