# 652. Find Duplicate Subtrees

Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.

Approach:
-if 2 subtrees are the same, then they'll have the same structure which can be compared using the traversals.
-if 2 trees have same traversal strings then they are duplicates

-create strings out of the tree traversals
-the strings are the keys of the dict
-if same is found in dict, append root to list