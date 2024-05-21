# 1325. Delete Leaves With a Given Value

Medium

Given a binary tree root and an integer target, delete all the leaf nodes with value target.

Note that once you delete a leaf node with value target, if its parent node becomes a leaf node and has the value target, it should also be deleted (you need to continue doing that until you cannot).

# Approach
- if a child node is a leaf and contains target then remove the branch
- if parent contains target and has no left or right child then remove the branch