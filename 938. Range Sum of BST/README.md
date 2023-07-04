# 938. Range Sum of BST

Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

Approach:
1. Traverse all nodes and compare with low and high and add to sum
2. Since it is a binary search tree, 
    - nodes along the left branch will always have values less than the node
    - nodes along right branch will always have values greater than the node
making use of this, check if nodes val is less or greater than the limits and traverse accordingly. 
When a node's val in within limits, sum it and move to its left and right branches