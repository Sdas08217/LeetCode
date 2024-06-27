# Find Center Of star Graph
class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        # The center node will be the common node in the first two edges
        # since the graph is a star graph.
        edge1 = edges[0]
        edge2 = edges[1]
