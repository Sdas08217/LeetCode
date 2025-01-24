from typing import List
from collections import deque

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        reverse_graph = [[] for _ in range(n)]
        in_degree = [0] * n
        
        # Build the reverse graph and compute in-degrees
        for node in range(n):
            for neighbor in graph[node]:
                reverse_graph[neighbor].append(node)
            in_degree[node] = len(graph[node])
        
        # Initialize a queue for nodes with zero out-degree (terminal nodes)
        queue = deque()
        for node in range(n):
            if in_degree[node] == 0:
                queue.append(node)
        
        # List to track safe nodes
        safe_nodes = []
        
        while queue:
            node = queue.popleft()
            safe_nodes.append(node)
            # Process predecessors in the reverse graph
            for predecessor in reverse_graph[node]:
                in_degree[predecessor] -= 1
                if in_degree[predecessor] == 0:
                    queue.append(predecessor)
        
        # Return safe nodes sorted in ascending order
        return sorted(safe_nodes)
