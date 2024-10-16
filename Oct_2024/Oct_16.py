# Longest Happy String
import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # Create a max-heap with (-count, char) to prioritize the largest count
        max_heap = []
        if a > 0:
            heapq.heappush(max_heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(max_heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(max_heap, (-c, 'c'))
        
        result = []  # Store the resulting happy string
        
        while max_heap:
            # Pop the character with the highest remaining count
            count1, char1 = heapq.heappop(max_heap)
            if len(result) >= 2 and result[-1] == result[-2] == char1:
                # If adding this character would cause three consecutive, try the next one
                if not max_heap:
                    break  # No other characters available to switch, stop
                count2, char2 = heapq.heappop(max_heap)
                result.append(char2)  # Add the second most frequent character
                if count2 + 1 < 0:  # Push back if there are more occurrences left
                    heapq.heappush(max_heap, (count2 + 1, char2))
                heapq.heappush(max_heap, (count1, char1))  # Push back the first character
            else:
                # Add the most frequent character to the result
                result.append(char1)
                if count1 + 1 < 0:  # Push back if more occurrences are left
                    heapq.heappush(max_heap, (count1 + 1, char1))
        
        return "".join(result)

  # Example usage:
solution = Solution()
print(solution.longestDiverseString(1, 1, 7))  # Output: "ccaccbcc"
print(solution.longestDiverseString(7, 1, 0))  # Output: "aabaa"
