# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        first, slow, fast = head, head, head
        count = 1
        while count<k:
            fast = fast.next
            first = first.next
            count+=1
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        first.val, slow.val = slow.val, first.val
        return head