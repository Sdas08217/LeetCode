# Delete Nodes And Return Forest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        to_delete_set = set(to_delete)
        forest = []

        def helper(node, is_root):
            if not node:
                return None
            
            # Check if this node needs to be a new root
            root_deleted = node.val in to_delete_set
            if is_root and not root_deleted:
                forest.append(node)
            
            # Recur for left and right subtrees
            node.left = helper(node.left, root_deleted)
            node.right = helper(node.right, root_deleted)
            
            return None if root_deleted else node

        helper(root, True)
        return forest

# Helper function to print the tree (pre-order traversal)
def print_tree(node):
    if not node:
        return []
    return [node.val] + print_tree(node.left) + print_tree(node.right)

# Example Usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

to_delete = [3, 5]

solution = Solution()
forest = solution.delNodes(root, to_delete)

for tree in forest:
    print(print_tree(tree))
