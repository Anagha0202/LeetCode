# 110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

Approach 1:
-DFS trav each node and when condition false set flag to false 
-return flag as final answer
-height of null node = -1

Approach 2:
-DFS trav the tree and return the bool balance and height of tree
-null tree height = 0
-when   ->its left subtree returns False
        ->its right subtree returns False
        ->abs(left height- right height) > 1 
    set Balance to False
-final answer is the balance