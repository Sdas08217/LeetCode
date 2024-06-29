# All Ancestors of a Node in a Directed Acyclic Graph
class Solution(object):
    def getAncestors(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """
        # Step 1: Build the graph and initialize in-degrees
        graph = defaultdict(list)
        in_degree = [0] * n
        
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1
        
        # Step 2: Topological sorting using Kahn's algorithm (BFS-based)
        topo_order = []
        queue = deque([i for i in range(n) if in_degree[i] == 0])
        
        while queue:
            node = queue.popleft()
            topo_order.append(node)
            
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Step 3: Process nodes in topological order to find ancestors
        ancestors = [set() for _ in range(n)]
        
        for node in topo_order:
            for neighbor in graph[node]:
                # Add all ancestors of the current node to its neighbor
                ancestors[neighbor].update(ancestors[node])
                # Add the current node as an ancestor of its neighbor
                ancestors[neighbor].add(node)
        
        # Step 4: Convert sets to sorted lists
        result = [sorted(list(ancestor_set)) for ancestor_set in ancestors]
        
        return result

# Example usage:
sol = Solution()

# Example 1
n1 = 8
edges1 = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
print(sol.getAncestors(n1, edges1))  # Output: [[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]]

# Example 2
n2 = 5
edges2 = [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
print(sol.getAncestors(n2, edges2))  # Output: [[],[0],[0,1],[0,1,2],[0,1,2,3]]
