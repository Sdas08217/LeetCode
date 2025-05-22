from typing import List
import heapq

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n, m = len(nums), len(queries)

        # Step 1: Check if it's possible at all by computing full coverage
        diff = [0] * (n + 1)
        for l, r in queries:
            diff[l] += 1
            if r + 1 < n:
                diff[r + 1] -= 1

        coverage = [0] * n
        curr = 0
        for i in range(n):
            curr += diff[i]
            coverage[i] = curr
            if coverage[i] < nums[i]:
                return -1  # Not enough queries to satisfy nums[i]

        # Step 2: Greedy selection of minimal required queries
        start_buckets = [[] for _ in range(n)]
        for l, r in queries:
            start_buckets[l].append(r)

        diff = [0] * (n + 1)
        curr_cov = 0
        used = 0
        max_heap = []

        for i in range(n):
            for r in start_buckets[i]:
                heapq.heappush(max_heap, -r)
            curr_cov += diff[i]
            if curr_cov >= nums[i]:
                continue
            need = nums[i] - curr_cov
            for _ in range(need):
                if not max_heap:
                    return -1
                r = -heapq.heappop(max_heap)
                used += 1
                curr_cov += 1
                if r + 1 < n:
                    diff[r + 1] -= 1

        return m - used
