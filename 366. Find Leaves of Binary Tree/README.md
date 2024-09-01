# 366. Find Leaves of Binary Tree 🔒
Medium
Topics: DFS
Companies: Google

Given the root of a binary tree, collect a tree's nodes as if you were doing this:

Collect all the leaf nodes.
Remove all the leaf nodes.
Repeat until the tree is empty.
 
Example 1:
Input: root = [1,2,3,4,5]
Output: [[4,5,3],[2],[1]]
Explanation:
[[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per each level it does not matter the order on which elements are returned.

# Approach:
- Traverse the tree and calculate the position of each node in the final result
- leaf nodes are always at position 0, n-1 parent nodes are always at position 1 and so no
- add each node values into specific positions in the result list