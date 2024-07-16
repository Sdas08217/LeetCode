# Step-By-Step Directions From a Binary Tree Node to Another
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def getDirections(self, root, startValue, destValue):
        """
        :type root: TreeNode
        :type startValue: int
        :type destValue: int
        :rtype: str
        """
        # Find the Lowest Common Ancestor (LCA) of the startValue and destValue
        def findLCA(node, p, q):
            if not node or node.val == p or node.val == q:
                return node
            left = findLCA(node.left, p, q)
            right = findLCA(node.right, p, q)
            if left and right:
                return node
            return left if left else right

        # Find the path from the given node to the target value
        def findPath(node, val, path):
            if not node:
                return False
            if node.val == val:
                return True
            path.append('L')
            if findPath(node.left, val, path):
                return True
            path.pop()
            path.append('R')
            if findPath(node.right, val, path):
                return True
            path.pop()
            return False

        # Find the LCA
        lca = findLCA(root, startValue, destValue)

        # Find the path from LCA to startValue
        pathToStart = []
        findPath(lca, startValue, pathToStart)

        # Find the path from LCA to destValue
        pathToDest = []
        findPath(lca, destValue, pathToDest)

        # Convert pathToStart to 'U's
        pathToStart = ['U'] * len(pathToStart)

        # Combine the paths
        return ''.join(pathToStart) + ''.join(pathToDest)

# Example usage
root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(4)

solution = Solution()
startValue = 3
destValue = 6
print(solution.getDirections(root, startValue, destValue))  # Output: "UURL"
