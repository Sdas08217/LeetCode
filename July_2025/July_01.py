class Solution:
    def possibleStringCount(self, word: str) -> int:
        n = len(word)
        groups = []
        i = 0
        
        # Grouping consecutive characters with their count
        while i < n:
            j = i
            while j < n and word[j] == word[i]:
                j += 1
            groups.append((word[i], j - i))
            i = j
        
        total = 1  # Start with the original string itself
        for _, length in groups:
            if length > 1:
                total += (length - 1)  # Add all reduced versions for this group
        
        return total
