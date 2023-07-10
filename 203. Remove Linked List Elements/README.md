# 203. Remove Linked List Elements

Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

Approach:
-set a pointer to the root of the linked list
-using a prev pointer and current pointer
-when node.val==val set prev.next = curr.next