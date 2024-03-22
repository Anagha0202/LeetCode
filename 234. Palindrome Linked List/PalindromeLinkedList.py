# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Normal way to check for a palindrome is 2 pointers which travels towards the middle
        # We can create the same by reversing the pointing direction of the last half of the linked list
        #Hare and tortoise algorithm to find the middle of the list
        # Starting from the middle reverse the direction of last half of the list
        # Compare elements starting from begin and tail till mid
        # Space: O(1)
        tail, mid, begin = head, head, head
        while tail.next:
            if tail.next.next:
                tail = tail.next.next
            else: tail = tail.next
            mid = mid.next

        prev, mid = mid, mid.next
        prev.next = None
        while mid:
            temp = mid.next
            mid.next = prev
            prev = mid
            mid = temp
        
        while begin and tail:
            if begin.val!=tail.val:
                return False
            begin = begin.next
            tail = tail.next
        return True

        # Space : O(n) Approach
        node = head
        items = []
        while node:
            items.append(node.val)
            node = node.next
        return items == items[::-1]