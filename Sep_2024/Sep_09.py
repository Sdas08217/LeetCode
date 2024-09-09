# Spiral Matrix IV
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def spiralMatrix(self, m, n, head):
        """
        :type m: int
        :type n: int
        :type head: Optional[ListNode]
        :rtype: List[List[int]]
        """
        # Initialize the matrix with -1
        matrix = [[-1] * n for _ in range(m)]
        
        # Define the direction vectors for right, down, left, and up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Initialize the starting position and the direction index
        r, c, di = 0, 0, 0
        
        # Traverse the matrix in spiral order and fill values from the linked list
        current_node = head
        for _ in range(m * n):
            if current_node:
                matrix[r][c] = current_node.val
                current_node = current_node.next
            else:
                break
            
            # Calculate the next position
            nr, nc = r + directions[di][0], c + directions[di][1]
            
            # Check if the next position is out of bounds or already visited
            if not (0 <= nr < m and 0 <= nc < n and matrix[nr][nc] == -1):
                # Change direction (right -> down -> left -> up)
                di = (di + 1) % 4
                nr, nc = r + directions[di][0], c + directions[di][1]
            
            # Move to the next position
            r, c = nr, nc
        
        return matrix

  # Example Usage 
  # Define the linked list
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

# Link the nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

# Create an instance of the Solution class
solution = Solution()

# Define the matrix dimensions
m = 3  # Number of rows
n = 3  # Number of columns

# Get the spiral matrix
result = solution.spiralMatrix(m, n, node1)

# Print the result
for row in result:
    print(row)
Expected Output:
[1, 2, 3]
[6, -1, 4]
[5, -1, -1]
