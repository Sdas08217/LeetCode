# Largest Combination With Bitwise AND Greater Than Zero.
class Solution:
    def largestCombination(self, candidates):
        max_bits = 24  # Since candidates[i] <= 10^7, we only need 24 bits
        bit_counts = [0] * max_bits
        
        # Count the number of candidates that have each bit set
        for num in candidates:
            for bit in range(max_bits):
                if num & (1 << bit):
                    bit_counts[bit] += 1
        
        # The answer is the maximum count found in any bit position
        return max(bit_counts)

  # Example usage
solution = Solution()

# Sample input of candidate numbers
candidates = [16, 8, 4, 2, 1]

# Call the method to get the largest combination
result = solution.largestCombination(candidates)

print(f"The largest combination of bits set is: {result}")
