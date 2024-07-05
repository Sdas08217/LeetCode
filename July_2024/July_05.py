# Find the Minimum and Maximum Number of Nodes Between Critical Points
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        critical_points = []
        prev, curr, next = head, head.next, head.next.next
        index = 1  # the index of the curr node

        while next:
            if (curr.val > prev.val and curr.val > next.val) or (curr.val < prev.val and curr.val < next.val):
                critical_points.append(index)
            
            prev, curr, next = curr, next, next.next
            index += 1
        
        if len(critical_points) < 2:
            return [-1, -1]
        
        min_distance = float('inf')
        max_distance = critical_points[-1] - critical_points[0]
        
        for i in range(1, len(critical_points)):
            min_distance = min(min_distance, critical_points[i] - critical_points[i-1])
        
        return [min_distance, max_distance]

  # Example Usage
# Function to create a linked list from a list of values
def list_to_nodes(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head
