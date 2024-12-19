class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        max_seen = 0
        chunks = 0
        for i, val in enumerate(arr):
            max_seen = max(max_seen, val)
            # If the max value we've seen so far is equal to the index,
            # we can make a chunk.
            if max_seen == i:
                chunks += 1
        return chunks
# Example usage
solution = Solution()
print(solution.maxChunksToSorted([4, 3, 2, 1, 0]))  # Output: 1
print(solution.maxChunksToSorted([1, 0, 2, 3, 4]))  # Output: 4
