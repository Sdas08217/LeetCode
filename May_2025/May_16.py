from typing import List

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:

        def hamming_distance(word1, word2):
            # Calculate the Hamming distance between two words
            return sum(c1 != c2 for c1, c2 in zip(word1, word2))

        n = len(words)
        # Create a list of (index, word, group) tuples
        indexed_words = list(enumerate(words))

        # DP table to store the longest subsequence ending at each index
        dp = [[1, -1] for _ in range(n)]  # [length, previous index]

        # Build the DP table without sorting to maintain original order
        for i in range(n):
            for j in range(i):
                idx1, word1 = indexed_words[i]
                idx2, word2 = indexed_words[j]

                # Check conditions: different groups, equal length, Hamming distance of 1
                if (groups[idx1] != groups[idx2] and len(word1) == len(word2) and 
                    hamming_distance(word1, word2) == 1):
                    if dp[j][0] + 1 > dp[i][0]:
                        dp[i] = [dp[j][0] + 1, j]

        # Find the maximum length subsequence
        max_len, max_idx = max((length, idx) for idx, (length, _) in enumerate(dp))

        # Reconstruct the subsequence
        subsequence = []
        while max_idx != -1:
            subsequence.append(indexed_words[max_idx][1])
            max_idx = dp[max_idx][1]

        # Return the reversed subsequence as it was built backward
        return subsequence[::-1]
