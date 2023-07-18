# 19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Approach:
-use slow and fast pointer to locate the position on nth node
-slow starts at dummy null node
-fast starts at root+n th node
-both moves by 1 until fast reaches None => slow.next is the one to be removed