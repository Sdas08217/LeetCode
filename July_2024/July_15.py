# Create Binary Tree From Descriptions
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def createBinaryTree(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]
        """
        from collections import defaultdict
        
        # Dictionary to store value -> TreeNode
        nodes = {}
        # Set to track all children
        children = set()
        
        # Create nodes and connect them according to descriptions
        for parent_val, child_val, is_left in descriptions:
            if parent_val not in nodes:
                nodes[parent_val] = TreeNode(parent_val)
            if child_val not in nodes:
                nodes[child_val] = TreeNode(child_val)
            
            parent_node = nodes[parent_val]
            child_node = nodes[child_val]
            
            if is_left:
                parent_node.left = child_node
            else:
                parent_node.right = child_node
            
            # Add child_val to children set
            children.add(child_val)
        
        # The root is the node that is never a child
        for parent_val, child_val, is_left in descriptions:
            if parent_val not in children:
                return nodes[parent_val]

          # Example usage
descriptions1 = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
solution = Solution()
root1 = solution.createBinaryTree(descriptions1)
# This will return the root of the tree, you can then print or verify the structure

descriptions2 = [[1,2,1],[2,3,0],[3,4,1]]
root2 = solution.createBinaryTree(descriptions2)
# This will return the root of the tree, you can then print or verify the structure
