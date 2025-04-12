import math
from itertools import product

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        if n == 1:
            return sum(1 for d in range(1, 10) if d % k == 0)
        
        m = (n + 1) // 2
        good_freqs = set()

        # Generate first half of palindromes
        for first_half in product(range(1, 10), *([range(10)] * (m - 1))):
            # Construct palindrome
            if n % 2 == 0:
                palindrome_digits = first_half + first_half[::-1]
            else:
                palindrome_digits = first_half[:-1] + (first_half[-1],) + first_half[:-1][::-1]

            p = int(''.join(map(str, palindrome_digits)))

            if p % k == 0:
                freq = [0] * 10
                for d in palindrome_digits:
                    freq[d] += 1
                good_freqs.add(tuple(freq))

        total = 0
        for freq in good_freqs:
            total += self.count_valid_permutations(freq, n)
        return total

    def count_valid_permutations(self, freq, n):
        total = self.total_permutations(freq, n)
        if freq[0] == 0:
            return total  # no leading zero issue
        # Subtract permutations where leading digit is 0
        freq0 = list(freq)
        freq0[0] -= 1
        total_with_leading_zero = self.total_permutations(freq0, n - 1)
        return total - total_with_leading_zero

    def total_permutations(self, freq, n):
        res = math.factorial(n)
        for f in freq:
            res //= math.factorial(f)
        return res
