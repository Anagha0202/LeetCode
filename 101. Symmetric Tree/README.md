# 101. Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Input: root = [1,2,2,3,4,4,3]
Output: true

Approach:
-DFS
-Traverse the left and right subtrees simultaneously
-check if left==right, check opposite branches of each subtree
-base case: when both or one node is null