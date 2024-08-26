# N-ary Tree Postorder Traversal
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        result = []
        
        def traverse(node):
            if node:
                for child in node.children:
                    traverse(child)
                result.append(node.val)
        
        traverse(root)
        return result

  # Example usage:

# Define the tree
# Example 1: root = [1,null,3,2,4,null,5,6]
root = Node(1, [
    Node(3, [Node(5), Node(6)]),
    Node(2),
    Node(4)
])

# Create an instance of the Solution class
solution = Solution()

# Call the postorder method
output = solution.postorder(root)

# Print the result
print(output)  # Output: [5, 6, 3, 2, 4, 1]
