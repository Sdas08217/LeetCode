# Count the Number of Consistent Strings
class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        allowed_set = set(allowed)
        count = 0
        
        for word in words:
            if all(char in allowed_set for char in word):
                count += 1
                
        return count

  # Example usage of countConsistentStrings function
allowed = "abc"
words = ["a", "b", "c", "ab", "ac", "bc", "abc", "abcd"]

sol = Solution()
result = sol.countConsistentStrings(allowed, words)
print(result)
