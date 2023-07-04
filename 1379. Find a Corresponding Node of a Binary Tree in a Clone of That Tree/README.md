# 1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree

Given two binary trees original and cloned and given a reference to a node target in the original tree.

The cloned tree is a copy of the original tree.

Return a reference to the same node in the cloned tree.

Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.

Approach:
-Traverse the original tree and cloned tree until you find the original node that's equal to the target. 
-Question says all nodes have unique values, hence if target is found, return the same node from cloned.