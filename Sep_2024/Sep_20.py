# Shortest Palindrome
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        # Create a new string that is s + '#' + reversed(s)
        new_s = s + '#' + s[::-1]
        n = len(new_s)

        # Create the LPS (Longest Prefix Suffix) array
        lps = [0] * n
        j = 0  # Length of previous longest prefix suffix

        for i in range(1, n):
            while j > 0 and new_s[i] != new_s[j]:
                j = lps[j - 1]

            if new_s[i] == new_s[j]:
                j += 1
                lps[i] = j
            else:
                lps[i] = 0

        # The length of the longest palindromic prefix
        longest_palindromic_prefix_length = lps[-1]
        # Characters to add in front to make the palindrome
        to_add = s[longest_palindromic_prefix_length:][::-1]
        
        return to_add + s

# Example usage:
solution = Solution()
print(solution.shortestPalindrome("aacecaaa"))  # Output: "aaacecaaa"
print(solution.shortestPalindrome("abcd"))      # Output: "dcbabcd"
