from collections import defaultdict
from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        index = 2  # Start marking islands from index 2
        area_map = {0: 0}  # Map island index to its size

        def dfs(r, c, index):
            stack = [(r, c)]
            area = 0
            while stack:
                x, y = stack.pop()
                if grid[x][y] == 1:
                    grid[x][y] = index
                    area += 1
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                            stack.append((nx, ny))
            return area

        # Step 1: Identify islands and compute their sizes
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    area_map[index] = dfs(r, c, index)
                    index += 1
        
        max_area = max(area_map.values(), default=0)
        
        # Step 2: Try changing each 0 to 1 and compute max possible island
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen = set()
                    area = 1  # Changing 0 to 1
                    for dx, dy in directions:
                        nr, nc = r + dx, c + dy
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                            seen.add(grid[nr][nc])
                    area += sum(area_map[i] for i in seen)
                    max_area = max(max_area, area)
        
        return max_area
