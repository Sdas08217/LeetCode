from collections import defaultdict
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        # Step 1: Build adjacency list for the tree
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        # Step 2: Variables to keep track of visited nodes and count of components
        visited = [False] * n
        self.components = 0
        
        # Step 3: DFS function
        def dfs(node: int) -> int:
            visited[node] = True
            subtree_sum = values[node]  # Start with the value of the current node
            
            for neighbor in tree[node]:
                if not visited[neighbor]:
                    subtree_sum += dfs(neighbor)  # Accumulate subtree sum
            
            # If subtree sum is divisible by k, it can form a valid component
            if subtree_sum % k == 0:
                self.components += 1
                return 0  # Reset the sum as the component is detached
            
            return subtree_sum
        
        # Step 4: Start DFS from the root (node 0)
        dfs(0)
        
        # Return the total number of components
        return self.components
