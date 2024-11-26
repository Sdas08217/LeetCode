# Find Champion II
from typing import List
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # Step 1: Build graph and indegree array
        graph = {i: [] for i in range(n)}
        indegree = [0] * n
        
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
        
        # Step 2: Find all nodes with zero indegree
        zero_indegree = [i for i in range(n) if indegree[i] == 0]
        
        # If there is not exactly one node with zero indegree, return -1
        if len(zero_indegree) != 1:
            return -1
        
        # Step 3: Check if the unique node with zero indegree can reach all other nodes
        champion = zero_indegree[0]
        visited = set()
        
        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        dfs(champion)
        
        # If the number of visited nodes is less than n, it means the champion cannot reach all nodes
        if len(visited) != n:
            return -1
        
        return champion
