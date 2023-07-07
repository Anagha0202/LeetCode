# 98. Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.

Approach:
-DFS
-each node's values has t fall within a range of values
- -inf<root.val<inf => root can have any value
- all left branch value has to be less than the root 
    => -inf<node.val<root.val
-similarly all right branch value has to be grater than root
    => root.val<node.val<inf