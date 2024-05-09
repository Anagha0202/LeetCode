# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Approach 2: Recursive 
        # If we need to traverse the ll in the given direction, it implies that we can multiply the digit with 2 and add any remainder that might come from the next digit,.
        # So thinking of it as the next digit is providing the carry to the previous, it can be written recursively. 
        # The function will return the carry to the previous digit
        def carryCalc(node):
            pro = node.val*2
            if node.next:
                pro += carryCalc(node.next)
            node.val = pro%10
            return pro//10
        
        leftOverCarry = carryCalc(head)
        if leftOverCarry>0:
            return ListNode(leftOverCarry, head)
        else: 
            return head

        # Approach 1: Most direct
        # Reverse the number linked list 
        def reverseList(head):
            prev, node, nxt = None, head, None
            while node:
                nxt = node.next 
                node.next = prev
                prev = node
                node = nxt 
            return prev

        # Multiply by 2 starting from the end of the list 
        carry = 0 
        node = reverseList(head)
        res = None
        while node:
            temp = ListNode()
            temp.val = ((node.val * 2)%10) + carry 
            temp.next = res
            res = temp
            carry = (node.val*2)//10
            node = node.next
        if carry:
            temp = ListNode()
            temp.val = carry
            temp.next = res
            res = temp        
        return res