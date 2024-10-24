# Flip Equivalent Binary Trees
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Base case: if both nodes are null, they are flip equivalent
        if not root1 and not root2:
            return True
        # If one of the nodes is null, they are not flip equivalent
        if not root1 or not root2:
            return False
        # If the values of the roots do not match, they are not flip equivalent
        if root1.val != root2.val:
            return False
        
        # Check the two possibilities: no flip or flip
        return (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) or \
               (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))

  #Example Usage
  # Create trees using TreeNode class

# Tree 1: [1, 2, 3, 4, 5, 6, null, null, null, 7, 8]
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)
root1.right.left = TreeNode(6)
root1.left.right.left = TreeNode(7)
root1.left.right.right = TreeNode(8)

# Tree 2: [1, 3, 2, null, 6, 4, 5, null, null, null, null, 8, 7]
root2 = TreeNode(1)
root2.left = TreeNode(3)
root2.right = TreeNode(2)
root2.left.right = TreeNode(6)
root2.right.left = TreeNode(4)
root2.right.right = TreeNode(5)
root2.right.right.left = TreeNode(8)
root2.right.right.right = TreeNode(7)

# Check if the two trees are flip equivalent
solution = Solution()
result = solution.flipEquiv(root1, root2)
print(result)  # Output: True
