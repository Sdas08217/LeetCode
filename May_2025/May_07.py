from typing import List
import heapq

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])
        min_times = [[float('inf')] * m for _ in range(n)]
        min_times[0][0] = 0
        pq = [(0, 0, 0)]  # (time, row, col)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while pq:
            current_time, r, c = heapq.heappop(pq)

            if current_time > min_times[r][c]:
                continue

            if r == n - 1 and c == m - 1:
                return current_time

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m:
                    start_move_time = moveTime[nr][nc]
                    arrival_time = max(current_time + 1, start_move_time + 1)
                    if arrival_time < min_times[nr][nc]:
                        min_times[nr][nc] = arrival_time
                        heapq.heappush(pq, (arrival_time, nr, nc))

        return -1
