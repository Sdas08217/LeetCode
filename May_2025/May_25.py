from collections import Counter
from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter(words)
        length = 0
        used_center = False

        for word in list(count.keys()):
            rev = word[::-1]
            if word != rev:
                pairs = min(count[word], count[rev])
                length += pairs * 4
                count[word] -= pairs
                count[rev] -= pairs
            else:
                pairs = count[word] // 2
                length += pairs * 4
                count[word] -= pairs * 2

        # Check if we can place a symmetric word in the center
        for word in count:
            if word[0] == word[1] and count[word] > 0:
                length += 2
                break

        return length
