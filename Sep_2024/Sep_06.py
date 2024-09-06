# Delete Nodes From Linked List Present in Array
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Step 1: Convert nums array to a set for fast lookup
        num_set = set(nums)
        
        # Step 2: Create a dummy node to handle edge cases where the head might be removed
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        # Step 3: Traverse the list and remove nodes with values in nums
        while current and current.next:
            if current.next.val in num_set:
                # Skip the node with the value in nums
                current.next = current.next.next
            else:
                # Move to the next node
                current = current.next
        
        # Return the head of the modified list
        return dummy.next

  # Example usage:
nums = [1, 2, 3]
head = create_linked_list([1, 2, 3, 4, 5])

sol = Solution()
modified_head = sol.modifiedList(nums, head)

print_linked_list(modified_head)  # Output: [4, 5]
