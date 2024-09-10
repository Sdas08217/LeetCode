# Insert Greatest Common Divisors in Linked List
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head  # No need to insert if there's only one node

        def gcd(a, b):
            """Helper function to compute GCD using the Euclidean algorithm."""
            while b:
                a, b = b, a % b
            return a

        current = head
        while current and current.next:
            # Calculate GCD of current node value and next node value
            gcd_value = gcd(current.val, current.next.val)

            # Create new node with the GCD value
            gcd_node = ListNode(gcd_value)

            # Insert the new node between current and next
            gcd_node.next = current.next
            current.next = gcd_node

            # Move to the next pair (skip the newly inserted node)
            current = gcd_node.next

        return head

# Helper function to print the linked list (Python 2 compatible)
def printLinkedList(head):
    current = head
    while current:
        if current.next:
            print current.val, "->",
        else:
            print current.val
        current = current.next

# Example usage
head = ListNode(18, ListNode(6, ListNode(10, ListNode(3))))

print "Original Linked List:"
printLinkedList(head)

solution = Solution()
new_head = solution.insertGreatestCommonDivisors(head)

print "Linked List after inserting GCD nodes:"
printLinkedList(new_head)

#Example Usage
Original Linked List:
18 -> 6 -> 10 -> 3

Linked List after inserting GCD nodes:
18 -> 6 -> 6 -> 2 -> 10 -> 1 -> 3
