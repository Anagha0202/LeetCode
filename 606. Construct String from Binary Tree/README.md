# 606. Construct String from Binary Tree

Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree with the preorder traversal way, and return it.

Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the original binary tree.

Approach:
-DFS
-following traversal, add the val of the node and then the brackets
-if a node has only right child, add pair of empty braces
