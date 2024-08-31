# Most Stones Removed with Same Row or Column
class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        class UnionFind:
            def __init__(self, size):
                self.parent = list(range(size))
                self.rank = [1] * size
            
            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])  # Path compression
                return self.parent[x]
            
            def union(self, x, y):
                rootX = self.find(x)
                rootY = self.find(y)
                if rootX != rootY:
                    if self.rank[rootX] > self.rank[rootY]:
                        self.parent[rootY] = rootX
                    elif self.rank[rootX] < self.rank[rootY]:
                        self.parent[rootX] = rootY
                    else:
                        self.parent[rootY] = rootX
                        self.rank[rootX] += 1
        
        if not stones:
            return 0
        
        n = len(stones)
        uf = UnionFind(n)
        
        row_map = {}
        col_map = {}
        
        for i, (x, y) in enumerate(stones):
            if x in row_map:
                uf.union(i, row_map[x])
            if y in col_map:
                uf.union(i, col_map[y])
            row_map[x] = i
            col_map[y] = i
        
        # Count unique components
        unique_components = len(set(uf.find(i) for i in range(n)))
        
        # Maximum stones that can be removed is total stones minus the number of unique components
        return n - unique_components


# Create an instance of the Solution class
solution = Solution()

# Define test cases
test_case_1 = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
test_case_2 = [[0,0],[0,2],[1,1],[2,0],[2,2]]
test_case_3 = [[0,0]]

# Call the removeStones method and print the results
print(solution.removeStones(test_case_1))  # Output: 5
print(solution.removeStones(test_case_2))  # Output: 3
print(solution.removeStones(test_case_3))  # Output: 0
