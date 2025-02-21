from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.recovered_values = set()
        self.recover_tree(root, 0)  # Start recovery with root value as 0

    def recover_tree(self, node: Optional[TreeNode], value: int):
        """ Recovers the tree by assigning correct values to nodes. """
        if not node:
            return
        
        node.val = value
        self.recovered_values.add(value)  # Store valid values for quick lookup

        # Recover left and right subtrees
        self.recover_tree(node.left, 2 * value + 1)
        self.recover_tree(node.right, 2 * value + 2)

    def find(self, target: int) -> bool:
        """ Returns True if target exists in the recovered tree. """
        return target in self.recovered_values
