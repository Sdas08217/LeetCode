from collections import deque
from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []
        queue = deque([root])  # Initialize queue with the root node
        
        while queue:
            level_size = len(queue)
            max_value = float('-inf')  # Initialize max value for the current level
            
            for _ in range(level_size):
                node = queue.popleft()  # Get the next node from the queue
                max_value = max(max_value, node.val)  # Update the maximum value
                
                # Add child nodes to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(max_value)  # Append the largest value of the level to the result
        
        return result
