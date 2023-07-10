# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        root = None
        node = head
        prev = None
        while(node):
            if node.val!=val:
                if prev==None:
                    root = node
                prev = node
            else:
                if prev:
                    prev.next = node.next 
            node = node.next
        return root
