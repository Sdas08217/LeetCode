# Split a String Into the Max Number of Unique Substrings
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def backtrack(start: int, used: set) -> int:
            if start == len(s):
                return 0
            
            max_count = 0
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if substring not in used:
                    used.add(substring)  # Choose the substring
                    # Recur for the rest of the string
                    max_count = max(max_count, 1 + backtrack(end, used))
                    used.remove(substring)  # Backtrack
            
            return max_count
        
        return backtrack(0, set())


# Example usage of the Solution class
sol = Solution()

# Test case 1
s1 = "ababccc"
output1 = sol.maxUniqueSplit(s1)
print(f"Maximum unique split for '{s1}' is: {output1}")

# Test case 2
s2 = "aba"
output2 = sol.maxUniqueSplit(s2)
print(f"Maximum unique split for '{s2}' is: {output2}")

# Test case 3
s3 = "aa"
output3 = sol.maxUniqueSplit(s3)
print(f"Maximum unique split for '{s3}' is: {output3}")
