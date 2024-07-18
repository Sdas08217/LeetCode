# Number of Good Leaf Nodes Pairs
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def countPairs(self, root, distance):
        """
        :type root: TreeNode
        :type distance: int
        :rtype: int
        """
        def dfs(node):
            if not node:
                return [0] * (distance + 1)
            
            if not node.left and not node.right:  # Leaf node
                leaf_count = [0] * (distance + 1)
                leaf_count[1] = 1  # Distance to itself is 1
                return leaf_count
            
            left_distances = dfs(node.left)
            right_distances = dfs(node.right)
            
            # Count good pairs
            for l in range(1, distance):
                for r in range(1, distance):
                    if l + r <= distance:
                        good_pairs[0] += left_distances[l] * right_distances[r]
            
            # Aggregate distances for the current node
            result = [0] * (distance + 1)
            for i in range(1, distance):
                result[i + 1] = left_distances[i] + right_distances[i]
            
            return result
        
        good_pairs = [0]
        dfs(root)
        return good_pairs[0]

# Example usage:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)

distance = 3
sol = Solution()
print(sol.countPairs(root, distance))  # Output: 1
