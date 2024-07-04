# Merge Nodes in Between Zeros 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Initialize a dummy node to build the new linked list
        dummy = ListNode(0)
        current_new_list = dummy
        current_sum = 0
        
        # Skip the initial 0 node
        current = head.next
        
        while current:
            if current.val == 0:
                # When a 0 is found, it means we have completed a segment
                current_new_list.next = ListNode(current_sum)
                current_new_list = current_new_list.next
                # Reset current_sum for the next segment
                current_sum = 0
            else:
                # Sum up the values between 0s
                current_sum += current.val
            
            current = current.next
        
        return dummy.next
# Example usage:
# Creating the linked list [0,3,1,0,4,5,2,0]
head = ListNode(0)
head.next = ListNode(3)
head.next.next = ListNode(1)
head.next.next.next = ListNode(0)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next = ListNode(2)
head.next.next.next.next.next.next.next = ListNode(0)
