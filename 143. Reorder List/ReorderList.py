# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # finding the middle of the list 
        slow , fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # split the list and reverse second half 
        second = slow.next
        slow.next = None
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # combine both halves alternatively 
        first, second = head, prev
        while first and second:
            tempf = first.next
            temps = second.next 
            first.next = second
            second.next = tempf
            first = tempf
            second = temps