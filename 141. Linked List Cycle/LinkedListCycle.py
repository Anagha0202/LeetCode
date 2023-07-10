# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Approach 2:
        slow , fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                return True
        return False
        
        # Approach 1: 
        curr = head
        nodesList = {}
        while curr:
            if curr in nodesList:
                return True
            nodesList[curr] = True
            if curr.next==None:
                return False
            curr = curr.next