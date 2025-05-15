from typing import List

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        # Initialize the result list with the first word
        result = [words[0]]
        last_group = groups[0]

        # Iterate through the remaining elements
        for i in range(1, len(words)):
            # If the current group differs from the last selected group, add the word
            if groups[i] != last_group:
                result.append(words[i])
                last_group = groups[i]

        return result
