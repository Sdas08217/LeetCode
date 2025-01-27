from typing import List

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Initialize the transitive closure matrix with False
        reachable = [[False] * numCourses for _ in range(numCourses)]
        
        # Mark direct prerequisites as True
        for a, b in prerequisites:
            reachable[a][b] = True
        
        # Floyd-Warshall algorithm to compute transitive closure
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    # If course i is reachable to k and k is reachable to j, then i is reachable to j
                    reachable[i][j] = reachable[i][j] or (reachable[i][k] and reachable[k][j])
        
        # Answer the queries
        return [reachable[u][v] for u, v in queries]
