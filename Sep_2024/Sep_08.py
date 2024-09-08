# Split Linked List in Parts
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        # Step 1: Find the total length of the linked list
        total_length = 0
        current = head
        while current:
            total_length += 1
            current = current.next
        
        # Step 2: Determine the size of each part
        part_size = total_length // k  # Minimum size of each part
        remainder = total_length % k  # Number of parts that will have an extra node
        
        # Step 3: Split the list into parts
        parts = []
        current = head
        
        for i in range(k):
            part_head = current
            # Determine the size of the current part
            current_part_size = part_size + (1 if i < remainder else 0)
            
            # Move the current pointer to the end of this part
            for j in range(current_part_size - 1):
                if current:
                    current = current.next
            
            # Cut the list
            if current:
                next_part = current.next
                current.next = None
                current = next_part
            
            # Add this part to the result
            parts.append(part_head)
        
        return parts

  # Example Usage
# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to print the linked list parts
def print_linked_list_parts(parts):
    result = []
    for part in parts:
        current = part
        part_vals = []
        while current:
            part_vals.append(current.val)
            current = current.next
        result.append(part_vals)
    print(result)

# Creating the linked list
head = create_linked_list([1, 2, 3])

# Splitting the linked list
solution = Solution()
k = 5
parts = solution.splitListToParts(head, k)

# Outputting the result
print_linked_list_parts(parts)
