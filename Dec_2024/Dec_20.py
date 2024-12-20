class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Helper function for recursive level traversal
        def dfs(node1, node2, level):
            if not node1 or not node2:
                return
            
            # If the level is odd, swap the values of the nodes
            if level % 2 == 1:
                node1.val, node2.val = node2.val, node1.val
            
            # Recurse for the next level
            dfs(node1.left, node2.right, level + 1)
            dfs(node1.right, node2.left, level + 1)
        
        # Initiate the DFS from the root's left and right children
        if root:
            dfs(root.left, root.right, 1)
        return root
