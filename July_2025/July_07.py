import heapq
from typing import List

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # Sort events based on their start day
        events.sort()
        total_days = max(end for _, end in events)
        min_heap = []
        attended = 0
        i = 0  # pointer to events

        for day in range(1, total_days + 1):
            # Add all events that start today
            while i < len(events) and events[i][0] == day:
                heapq.heappush(min_heap, events[i][1])
                i += 1

            # Remove events that have already ended
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)

            # Attend the event that ends the earliest
            if min_heap:
                heapq.heappop(min_heap)
                attended += 1

        return attended
