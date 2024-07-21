# Build a Matrix With Conditions
from collections import defaultdict, deque

class Solution(object):
    def topological_sort(self, conditions, k):
        graph = defaultdict(list)
        in_degree = [0] * (k + 1)
        
        for u, v in conditions:
            graph[u].append(v)
            in_degree[v] += 1
        
        queue = deque([node for node in range(1, k + 1) if in_degree[node] == 0])
        order = []
        
        while queue:
            node = queue.popleft()
            order.append(node)
            
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(order) == k:
            return order
        else:
            return []
    
    def buildMatrix(self, k, rowConditions, colConditions):
        """
        :type k: int
        :type rowConditions: List[List[int]]
        :type colConditions: List[List[int]]
        :rtype: List[List[int]]
        """
        row_order = self.topological_sort(rowConditions, k)
        col_order = self.topological_sort(colConditions, k)
        
        if not row_order or not col_order:
            return []
        
        row_pos = {num: i for i, num in enumerate(row_order)}
        col_pos = {num: i for i, num in enumerate(col_order)}
        
        matrix = [[0] * k for _ in range(k)]
        
        for num in range(1, k + 1):
            matrix[row_pos[num]][col_pos[num]] = num
        
        return matrix

# Example usage:
sol = Solution()
k = 3
rowConditions = [[1, 2], [3, 2]]
colConditions = [[2, 1], [3, 2]]
print(sol.buildMatrix(k, rowConditions, colConditions))
