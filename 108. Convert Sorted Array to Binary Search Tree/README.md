# 108. Convert Sorted Array to Binary Search Tree

Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced
Height-Balanced
A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
binary search tree.

Approach:
-2 pointer + Binary Search + DFS
-Since array is sorted, taking mid point will get us the root of each subtree
-create the tree starting from the mid point
-from the mid point, recursively create the left and right subtrees
-to check if anymore trees are possible on left or right, l<=r, the points should not have crossed each other