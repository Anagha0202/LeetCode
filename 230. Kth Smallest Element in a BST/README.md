# 230. Kth Smallest Element in a BST

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Approach:
-basic preorder of a BST gives the ascending order of the values in the tree
-Utilising stack to keep track of the parent nodes
-go down the left branch until there is not left branch and then pop the last node
-visit node.right 