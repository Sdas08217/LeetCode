# Find Kth Bit in Nth Binary String
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # Helper function to solve the problem recursively
        def findBit(n, k):
            if n == 1:  # Base case, S1 is "0"
                return '0'
            mid = (1 << (n - 1))  # 2^(n-1), middle index of the string
            if k == mid:
                return '1'  # Middle element is always '1'
            elif k < mid:
                return findBit(n - 1, k)  # Recur on the first half
            else:
                # If k is in the second half, find the mirrored position
                # in the first half and invert it
                mirrored_pos = 2 * mid - k
                return '1' if findBit(n - 1, mirrored_pos) == '0' else '0'

        return findBit(n, k)

# Example usage:
sol = Solution()
print(sol.findKthBit(3, 1))  # Output: "0"
print(sol.findKthBit(4, 11))  # Output: "1"
