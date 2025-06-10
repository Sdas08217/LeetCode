from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)

        # Extract frequencies with odd and even values
        odd_freqs = [count for count in freq.values() if count % 2 == 1]
        even_freqs = [count for count in freq.values() if count % 2 == 0]

        # According to constraints, both lists will have at least one element
        max_odd = max(odd_freqs)
        min_even = min(even_freqs)

        return max_odd - min_even
