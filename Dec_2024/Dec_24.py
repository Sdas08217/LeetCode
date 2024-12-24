from collections import defaultdict, deque
from typing import List

class Solution:
    def tree_diameter(self, edges: List[List[int]]) -> int:
        if not edges:
            return 0

        # Build adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def bfs(node: int) -> (int, int):
            visited = set()
            queue = deque([(node, 0)])
            visited.add(node)
            farthest_node = node
            max_dist = 0
            
            while queue:
                current, dist = queue.popleft()
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, dist + 1))
                        if dist + 1 > max_dist:
                            max_dist = dist + 1
                            farthest_node = neighbor
            return farthest_node, max_dist

        # First BFS to find one endpoint of the diameter
        start, _ = bfs(0)
        # Second BFS to find the diameter
        _, diameter = bfs(start)
        
        return diameter

    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        # Step 1: Calculate diameters of both trees
        diameter1 = self.tree_diameter(edges1)
        diameter2 = self.tree_diameter(edges2)
        
        # Step 2: Calculate radii of both trees
        radius1 = (diameter1 + 1) // 2
        radius2 = (diameter2 + 1) // 2
        
        # Step 3: Calculate minimum possible diameter of the combined tree
        return max(diameter1, diameter2, radius1 + radius2 + 1)

# Example usage
solution = Solution()
edges1 = [[0, 1], [0, 2], [0, 3]]
edges2 = [[0, 1]]
print(solution.minimumDiameterAfterMerge(edges1, edges2))  # Output: 3

edges1 = [[0, 1], [0, 2], [0, 3], [2, 4], [2, 5], [3, 6], [2, 7]]
edges2 = [[0, 1], [0, 2], [0, 3], [2, 4], [2, 5], [3, 6], [2, 7]]
print(solution.minimumDiameterAfterMerge(edges1, edges2))  # Output: 5
