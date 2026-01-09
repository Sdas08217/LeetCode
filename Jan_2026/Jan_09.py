class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node):
            # returns (subtree_root, depth)
            if not node:
                return None, 0
            
            left_node, left_depth = dfs(node.left)
            right_node, right_depth = dfs(node.right)
            
            if left_depth > right_depth:
                return left_node, left_depth + 1
            elif right_depth > left_depth:
                return right_node, right_depth + 1
            else:
                # both sides have deepest nodes
                return node, left_depth + 1
        
        return dfs(root)[0]
