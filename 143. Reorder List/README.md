# 143. Reorder List

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Approach:
-split the list into 2 halves
-find the middle of the list using: slow pointer moves by 1 and fast pointer moves by 2 => when fast pointer reaches the end of the list, slow will be at the middle => slow.next gives second half of the list
-reverse thesecond half of the list -> front pointer and end pointer to traverse the first half of the list in order and last half of the list in reverse order 