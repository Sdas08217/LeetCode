from collections import defaultdict, deque
from typing import List

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = defaultdict(list)
        in_degree = [0] * n

        # Step 1: Build the graph and compute in-degrees
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1

        # Step 2: Initialize a 2D array to track the max count of each color (26 letters) for each node
        color_count = [[0] * 26 for _ in range(n)]
        queue = deque()

        # Step 3: Initialize the queue with nodes having in-degree 0
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)
            # Initialize the count for the color of the node itself
            color_count[i][ord(colors[i]) - ord('a')] = 1

        visited = 0
        max_color_value = 0

        # Step 4: Process nodes in topological order
        while queue:
            node = queue.popleft()
            visited += 1

            # Update the result with the max color count at this node
            max_color_value = max(max_color_value, max(color_count[node]))

            # Traverse all neighbors
            for neighbor in graph[node]:
                for c in range(26):
                    # Update the color count for the neighbor
                    current_color = ord(colors[neighbor]) - ord('a')
                    add = 1 if c == current_color else 0
                    color_count[neighbor][c] = max(
                        color_count[neighbor][c],
                        color_count[node][c] + add
                    )

                # Decrease in-degree and add to queue if it's zero
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 5: If not all nodes were visited, there's a cycle
        return max_color_value if visited == n else -1
