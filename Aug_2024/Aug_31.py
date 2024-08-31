# Path with Maximum Probability
import heapq
from collections import defaultdict

class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start_node: int
        :type end_node: int
        :rtype: float
        """
        # Graph representation
        graph = defaultdict(list)
        for i, (a, b) in enumerate(edges):
            prob = succProb[i]
            graph[a].append((b, prob))
            graph[b].append((a, prob))
        
        # Priority queue (max-heap) and probability dictionary
        max_heap = [(-1.0, start_node)]  # (negative probability, node)
        probabilities = {i: 0.0 for i in range(n)}
        probabilities[start_node] = 1.0
        
        while max_heap:
            current_prob, node = heapq.heappop(max_heap)
            current_prob = -current_prob
            
            # If we reached the end node, return its probability
            if node == end_node:
                return current_prob
            
            # Explore neighbors
            for neighbor, prob in graph[node]:
                new_prob = current_prob * prob
                if new_prob > probabilities[neighbor]:
                    probabilities[neighbor] = new_prob
                    heapq.heappush(max_heap, (-new_prob, neighbor))
        
        # If we exit the loop without finding a path to `end_node`, return 0
        return 0.0

  # Example 1
n = 3
edges = [[0, 1], [1, 2], [0, 2]]
succProb = [0.5, 0.5, 0.2]
start_node = 0
end_node = 2

sol = Solution()
result = sol.maxProbability(n, edges, succProb, start_node, end_node)
print(result)  # Output: 0.25000

# Example 2
n = 3
edges = [[0, 1], [1, 2], [0, 2]]
succProb = [0.5, 0.5, 0.3]
start_node = 0
end_node = 2

sol = Solution()
result = sol.maxProbability(n, edges, succProb, start_node, end_node)
print(result)  # Output: 0.30000

# Example 3
n = 3
edges = [[0, 1]]
succProb = [0.5]
start_node = 0
end_node = 2

sol = Solution()
result = sol.maxProbability(n, edges, succProb, start_node, end_node)
print(result)  # Output: 0.00000
