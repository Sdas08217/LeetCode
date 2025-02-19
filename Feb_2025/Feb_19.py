class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        happy_strings = []
        
        def backtrack(current):
            if len(current) == n:
                happy_strings.append(current)
                return
            for ch in "abc":
                if not current or current[-1] != ch:
                    backtrack(current + ch)

        backtrack("")
        
        return happy_strings[k - 1] if k <= len(happy_strings) else ""

# Example Cases
sol = Solution()
print(sol.getHappyString(1, 3))  # Output: "c"
print(sol.getHappyString(1, 4))  # Output: ""
print(sol.getHappyString(3, 9))  # Output: "cab"
