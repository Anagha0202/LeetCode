# 310. Minimum Height Trees

Medium

A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

# Approach:
- root to the lowest leaf is the height of tree 
- starting from any leaf node, move towards the root 
    -> remove connecting edges from the leaf to other nodes
    -> by processing of elimating all leaf nodes, ultimatley will be left with either 1 or 2 nodes (2 because that is the smallest tree possible)
    -> return the remaining leaves as the possible roots
