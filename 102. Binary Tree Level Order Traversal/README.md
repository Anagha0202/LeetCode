# 102. Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Approach:
-BFS 
-BFS to traverse horizontally
-queue keeps track of the next node to be explored
-at the beginning of each level the len of the queue gives the number of nodes in that level
=> len of queue can give the nodes at each level of the tree