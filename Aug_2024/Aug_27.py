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
        # Create graph representation
        graph = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))
        
        # Priority queue (max-heap)
        max_heap = [(-1, start_node)]  # (negative probability, node)
        max_prob = [0] * n
        max_prob[start_node] = 1
        
        while max_heap:
            prob, node = heapq.heappop(max_heap)
            prob = -prob
            
            if node == end_node:
                return prob
            
            for neighbor, edge_prob in graph[node]:
                new_prob = prob * edge_prob
                if new_prob > max_prob[neighbor]:
                    max_prob[neighbor] = new_prob
                    heapq.heappush(max_heap, (-new_prob, neighbor))
        
        return 0.0

  # Example usage of the Solution class

# Create an instance of the Solution class
solution = Solution()

# Define the input parameters
n = 3
edges = [[0, 1], [1, 2], [0, 2]]
succProb = [0.5, 0.5, 0.2]
start_node = 0
end_node = 2

# Call the maxProbability method and print the result
result = solution.maxProbability(n, edges, succProb, start_node, end_node)
print("The maximum probability of success from node {} to node {} is: {:.5f}".format(start_node, end_node, result))
