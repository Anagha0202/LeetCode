# 543. Diameter of Binary Tree

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Approach:
-DFS
-Start from bottom up and find the diameter and height of each node
-height of null nodes = -1
-height of leaf nodes = 0
-height of a given node = max(left height , right height) + 1 -> adding height of itself
-calculate diameter at each nodes considering each node as the root of its own subtree
-diameter of given node = left height + right height + 2 -> adding 2 because 1 left branch and 1 right branch
-max of diameter at each node => result