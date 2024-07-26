# Find the City With the Smallest Number of Neighbors at a Threshold Distance
class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        # Step 1: Initialize the distance matrix
        dist = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0

        # Step 2: Populate the distance matrix with the given edges
        for fromi, toi, weighti in edges:
            dist[fromi][toi] = weighti
            dist[toi][fromi] = weighti

        # Step 3: Apply the Floyd-Warshall algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        # Step 4: Count reachable cities within the distance threshold for each city
        min_reachable = float('inf')
        best_city = -1
        
        for i in range(n):
            reachable = sum(1 for j in range(n) if dist[i][j] <= distanceThreshold)
            # We subtract 1 to exclude the city itself
            if reachable < min_reachable or (reachable == min_reachable and i > best_city):
                min_reachable = reachable
                best_city = i

        return best_city

# Example usage
solution = Solution()
n = 4
edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
distanceThreshold = 4
print(solution.findTheCity(n, edges, distanceThreshold))  # Output: 3

n = 5
edges = [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]]
distanceThreshold = 2
print(solution.findTheCity(n, edges, distanceThreshold))  # Output: 0
