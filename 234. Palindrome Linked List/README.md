# 234. Palindrome Linked List

Easy

Given the head of a singly linked list, return true if it is a palindrome  or false otherwise.

# Approach
- Normal way to check for a palindrome is 2 pointers which travels towards the middle
- We can create the same by reversing the pointing direction of the last half of the linked list
- Hare and tortoise algorithm to find the middle of the list
- Starting from the middle reverse the direction of last half of the list
- Compare elements starting from begin and tail till mid