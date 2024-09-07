# Linked List in Binary Tree
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSubPath(self, head, root):
        """
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """
        # Helper function to check if the linked list is a downward path starting from the current tree node
        def dfs(head, root):
            if not head:
                return True  # If we've reached the end of the list, the path is matched
            if not root:
                return False  # If we hit the end of the tree before matching the list
            if head.val != root.val:
                return False  # If the current values don't match

            # Recur for both left and right subtree
            return dfs(head.next, root.left) or dfs(head.next, root.right)

        # If the current root starts a valid path, or check in the left and right subtrees
        if not root:
            return False
        
        return dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

  # Create the linked list: 4 -> 2 -> 8
head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(8)

# Create the binary tree:
#        1
#       / \
#      4   4
#       \  /
#       2 2
#      / \
#     1   6
#          \
#           8
root = TreeNode(1)
root.left = TreeNode(4)
root.right = TreeNode(4)
root.left.right = TreeNode(2)
root.right.left = TreeNode(2)
root.left.right.left = TreeNode(1)
root.left.right.right = TreeNode(6)
root.left.right.right.right = TreeNode(8)

# Create an instance of the Solution class and call isSubPath
solution = Solution()
result = solution.isSubPath(head, root)

# Output the result
print(result)  # Expected output: True
