# Binary Tree Postorder Traversal
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self._postorder_helper(root, result)
        return result
    
    def _postorder_helper(self, node, result):
        if node:
            # Traverse the left subtree
            self._postorder_helper(node.left, result)
            # Traverse the right subtree
            self._postorder_helper(node.right, result)
            # Visit the node
            result.append(node.val)

# Example usage:
# root = TreeNode(1)
# root.right = TreeNode(2)
# root.right.left = TreeNode(3)
# sol = Solution()
# print(sol.postorderTraversal(root))  # Output: [3, 2, 1]
