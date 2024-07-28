# Second Minimum Time to Reach Destination
class Solution(object):
    def secondMinimum(self, n, edges, time, change):
        from collections import deque, defaultdict
        
        def bfs(adj, start):
            dist = [[float('inf')] * 2 for _ in range(n)]
            dist[start][0] = 0
            q = deque([(start, 0)])
            
            while q:
                node, d = q.popleft()
                for neighbor in adj[node]:
                    if dist[neighbor][0] > d + 1:
                        dist[neighbor][1] = dist[neighbor][0]
                        dist[neighbor][0] = d + 1
                        q.append((neighbor, d + 1))
                    elif dist[neighbor][0] < d + 1 < dist[neighbor][1]:
                        dist[neighbor][1] = d + 1
                        q.append((neighbor, d + 1))
            
            return dist
        
        def calc_time(time, change, dist):
            result = 0
            for _ in range(dist):
                if (result // change) % 2 == 1:  # If in red light phase
                    result = ((result // change) + 1) * change
                result += time
            return result

        # Create adjacency list
        adj = defaultdict(list)
        for u, v in edges:
            adj[u-1].append(v-1)
            adj[v-1].append(u-1)
        
        dist = bfs(adj, 0)
        
        # The second shortest distance to node n-1
        second_shortest_dist = dist[n-1][1]
        
        return calc_time(time, change, second_shortest_dist)

# Example usage
solution = Solution()
n = 5
edges = [[3,1],[1,4],[5,4],[3,2],[1,2],[2,5],[3,5]]
time = 5
change = 4
print(solution.secondMinimum(n, edges, time, change))  # Expected output based on problem conditions
