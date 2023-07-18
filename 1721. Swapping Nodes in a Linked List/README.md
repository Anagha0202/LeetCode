# 1721. Swapping Nodes in a Linked List

You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

Approach:
-2 pointers ->slow starts from beginning
            ->fast starts from head+k 
            =>creates a window of size k
            =>when fast reaches the end of the list, slow is k behind => at kth node from end
-3rd pointer to point to kth node from beginning
