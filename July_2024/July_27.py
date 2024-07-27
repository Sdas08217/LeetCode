# Minimum Cost to Convert String I
class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        """
        :type source: str
        :type target: str
        :type original: List[str]
        :type changed: List[str]
        :type cost: List[int]
        :rtype: int
        """
        import sys
        
        # Number of distinct lowercase English letters
        ALPHABET_SIZE = 26
        INF = sys.maxsize
        
        # Create a cost matrix initialized with infinity
        transformation_cost = [[INF] * ALPHABET_SIZE for _ in range(ALPHABET_SIZE)]
        
        # Set the cost of transforming a character to itself to 0
        for i in range(ALPHABET_SIZE):
            transformation_cost[i][i] = 0
        
        # Fill the transformation cost from the given original, changed, and cost arrays
        for o, c, z in zip(original, changed, cost):
            from_char = ord(o) - ord('a')
            to_char = ord(c) - ord('a')
            transformation_cost[from_char][to_char] = min(transformation_cost[from_char][to_char], z)
        
        # Floyd-Warshall algorithm to find all-pairs shortest paths
        for k in range(ALPHABET_SIZE):
            for i in range(ALPHABET_SIZE):
                for j in range(ALPHABET_SIZE):
                    if transformation_cost[i][k] < INF and transformation_cost[k][j] < INF:
                        transformation_cost[i][j] = min(transformation_cost[i][j], transformation_cost[i][k] + transformation_cost[k][j])
        
        # Calculate the total cost to convert source to target
        total_cost = 0
        for s_char, t_char in zip(source, target):
            s_idx = ord(s_char) - ord('a')
            t_idx = ord(t_char) - ord('a')
            if transformation_cost[s_idx][t_idx] == INF:
                return -1  # If we can't transform s_char to t_char
            total_cost += transformation_cost[s_idx][t_idx]
        
        return total_cost

# Example Usage:
sol = Solution()
source = "abcd"
target = "acbe"
original = ["a", "b", "c", "c", "e", "d"]
changed = ["b", "c", "b", "e", "b", "e"]
cost = [2, 5, 5, 1, 2, 20]

print(sol.minimumCost(source, target, original, changed, cost))  # Output: 28
