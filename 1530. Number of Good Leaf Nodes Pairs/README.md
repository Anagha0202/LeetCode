# 1530. Number of Good Leaf Nodes Pairs
Medium
Topics: DFS, Least Common Ancestor
Companies: Tiktok, Apple, ByteDance, Google

You are given the root of a binary tree and an integer distance. A pair of two different leaf nodes of a binary tree is said to be good if the length of the shortest path between them is less than or equal to distance.

Return the number of good leaf node pairs in the tree.

# Approach: 
- Least Common Ancestor - DFS
- Each leaf node: returns 1
- Each non-leaf node: return list of all connected leaf nodes that can be further considered given the distance constraint