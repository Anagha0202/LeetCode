# 112. Path Sum

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Approach:
-DFS
-traverse each node and subtract from target 
-if leaf node, check if target==0 => return True
-if null node, means target!=0 at leaf node => direct False