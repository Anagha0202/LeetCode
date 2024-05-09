# 2816. Double a Number Represented as a Linked List

Medium

You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.

Return the head of the linked list after doubling it.

# Approach:
- If we need to traverse the ll in the given direction, it implies that we can multiply the digit with 2 and add any remainder that might come from the next digit,.
- So thinking of it as the next digit is providing the carry to the previous, it can be written recursively. 
- The function will return the carry to the previous digit