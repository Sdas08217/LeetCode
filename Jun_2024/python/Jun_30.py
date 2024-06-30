# Remove Max Number of Edges to Keep Graph Fully Traversable
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False

class Solution(object):
    def maxNumEdgesToRemove(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        uf_alice = UnionFind(n + 1)
        uf_bob = UnionFind(n + 1)
        uf_combined = UnionFind(n + 1)
        
        redundant_edges = 0
        
        # Step 1: Add all type 3 edges to both Alice's and Bob's graphs
        for edge in edges:
            if edge[0] == 3:
                if not uf_combined.union(edge[1], edge[2]):
                    redundant_edges += 1
                else:
                    uf_alice.union(edge[1], edge[2])
                    uf_bob.union(edge[1], edge[2])
        
        # Step 2: Add type 1 edges to Alice's graph
        for edge in edges:
            if edge[0] == 1:
                if not uf_alice.union(edge[1], edge[2]):
                    redundant_edges += 1
        
        # Step 3: Add type 2 edges to Bob's graph
        for edge in edges:
            if edge[0] == 2:
                if not uf_bob.union(edge[1], edge[2]):
                    redundant_edges += 1
        
        # Check if both Alice and Bob can traverse the entire graph
        if all(uf_alice.find(i) == uf_alice.find(1) for i in range(2, n + 1)) and all(uf_bob.find(i) == uf_bob.find(1) for i in range(2, n + 1)):
            return redundant_edges
        else:
            return -1

      # Example usage:
solution = Solution()
n = 4
edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
print(solution.maxNumEdgesToRemove(n, edges))  # Output: 2
