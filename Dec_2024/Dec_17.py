# Construct String With Repeat Limit
from collections import Counter
import heapq

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        # Count the frequency of each character
        freq = Counter(s)
        
        # Max-heap based on characters (negative because heapq is a min-heap in Python)
        max_heap = [(-ord(char), char, count) for char, count in freq.items()]
        heapq.heapify(max_heap)
        
        result = []
        
        while max_heap:
            # Take the largest available character
            _, char, count = heapq.heappop(max_heap)
            
            # Add this character up to repeatLimit times
            add_count = min(count, repeatLimit)
            result.append(char * add_count)
            remaining = count - add_count
            
            if remaining > 0:
                # Look at the next largest character
                if max_heap:
                    _, next_char, next_count = heapq.heappop(max_heap)
                    
                    # Add the next largest character to break repetition
                    result.append(next_char)
                    if next_count - 1 > 0:
                        # Push the next character back if it still has remaining
                        heapq.heappush(max_heap, (-ord(next_char), next_char, next_count - 1))
                    
                    # Reinsert the current character with the remaining count
                    heapq.heappush(max_heap, (-ord(char), char, remaining))
                else:
                    # If no other character is available, stop
                    break
        
        return ''.join(result)
