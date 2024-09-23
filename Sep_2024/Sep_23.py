# Extra Characters in a String
class Solution(object):
    def minExtraChar(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: int
        """
        n = len(s)
        dp = [0] * (n + 1)

        # Initialize the DP array
        for i in range(n + 1):
            dp[i] = i  # In the worst case, all characters are extra

        word_set = set(dictionary)

        for i in range(1, n + 1):
            # Check every possible ending position of the substring
            for j in range(i):
                # If the substring s[j:i] is in the dictionary
                if s[j:i] in word_set:
                    dp[i] = min(dp[i], dp[j])  # Minimize extra characters

            # Calculate the extra characters if no valid word ends at i
            dp[i] = min(dp[i], dp[i - 1] + 1)  # Consider adding the current character as extra

        return dp[n]

  # Example usage
s1 = "leetscode"
dictionary1 = ["leet", "code", "leetcode"]
solution = Solution()
print(solution.minExtraChar(s1, dictionary1))  # Output: 1

s2 = "sayhelloworld"
dictionary2 = ["hello", "world"]
print(solution.minExtraChar(s2, dictionary2))  # Output: 3
