# Kth Largest Sum in a Binary Tree
from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        
        level_sums = []
        queue = deque([root])
        
        while queue:
            level_sum = 0
            for _ in range(len(queue)):  # Process all nodes at the current level
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level_sums.append(level_sum)
        
        if len(level_sums) < k:
            return -1
        
        # Sort level sums in descending order
        level_sums.sort(reverse=True)
        
        return level_sums[k - 1]

  # Example usage
k = 2
result = sol.kthLargestLevelSum(root, k)
print(f"The {k}th largest level sum is: {result}")
