# Cousins in Binary Tree II
from collections import deque
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        pq = deque()
        pq.append((root.val, root))
        
        while pq:
            n = len(pq)
            
			# calculate levelSum at each level
            levelSum = 0
            for localSum, node in pq:
                levelSum += node.val
                
            for i in range(n):
                localSum, node = pq.popleft()
                
				# calculate childSum
                childSum = 0
                if node.left: childSum += node.left.val
                if node.right: childSum += node.right.val
                
				# queue children with childSum
                if node.left: pq.append((childSum, node.left))
                if node.right: pq.append((childSum, node.right))
                   
				# new node value is levelSum - localSum
                node.val = levelSum - localSum
                 
        return root


# Example Usage
if __name__ == "__main__":
    # Creating a binary tree:
    #       1
    #      / \
    #     2   3
    #    / \   \
    #   4   5   6
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    
    print("Original tree values:")
    print_tree_level_order(root)
    
    # Replace values in tree
    sol = Solution()
    new_root = sol.replaceValueInTree(root)
    
    print("\nTree values after replacement:")
    print_tree_level_order(new_root)
