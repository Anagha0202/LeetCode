# 105. Construct Binary Tree from Preorder and Inorder Traversal

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Approach:
-preorder -> root, left, right => first value gives the root of the whole tree
-inorder -> left, root, right => using root from preorder, split the inorder based on root
    ->count of elements of the left and right in inorder gives each branch
    ->use this to split preorder into left and right branch