from collections import deque
from typing import List

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]],
                   containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)
        visited = set()
        haveBoxes = set(initialBoxes)
        hasKey = set()
        queue = deque()

        # Add initially open boxes to the processing queue
        for box in initialBoxes:
            if status[box] == 1:
                queue.append(box)

        totalCandies = 0

        while queue:
            box = queue.popleft()
            if box in visited:
                continue
            visited.add(box)

            # Collect candies from this box
            totalCandies += candies[box]

            # Collect keys and check if they open any box we already have
            for key in keys[box]:
                if key not in hasKey:
                    hasKey.add(key)
                    if key in haveBoxes and key not in visited:
                        queue.append(key)

            # Add contained boxes: open immediately if we can
            for newBox in containedBoxes[box]:
                if newBox not in haveBoxes:
                    haveBoxes.add(newBox)
                if status[newBox] == 1 or newBox in hasKey:
                    if newBox not in visited:
                        queue.append(newBox)

        return totalCandies
