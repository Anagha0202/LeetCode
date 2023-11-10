# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        r = res
        temp1 = l1
        temp2 = l2
        nextcarry = 0

        while temp1 or temp2:
            t1, t2 = 0, 0
            if temp1:
                t1 = temp1.val
                temp1 = temp1.next
            if temp2:
                t2 = temp2.val
                temp2 = temp2.next
            
            nextcarry += t1+t2
            tempRes = ListNode(nextcarry%10)
            r.next = tempRes
            r = tempRes
            nextcarry = nextcarry//10             

        if nextcarry!=0:
            tempRes = ListNode(nextcarry)
            r.next = tempRes
            r = tempRes
        return res.next
        