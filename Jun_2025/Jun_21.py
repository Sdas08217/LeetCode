from collections import Counter

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = Counter(word)
        values = list(freq.values())
        min_deletions = float('inf')

        for target in range(1, max(values) + 1):
            deletions = 0
            for v in values:
                if v < target:
                    deletions += v  # delete all, can't increase
                elif v > target + k:
                    deletions += v - (target + k)  # delete extra
                # else in [target, target + k] → no deletion
            min_deletions = min(min_deletions, deletions)

        return min_deletions
