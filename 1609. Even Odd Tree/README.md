# 1609. Even Odd Tree

Medium

A binary tree is named Even-Odd if it meets the following conditions:

The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, etc.
For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).
Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.

# Approach
- Requires level order traversal as the values in each level have to be checked => BFS
- Level number (odd or even) defines which condition is to be checked 
    -> odd - even values and descending order
    -> even - odd values and ascending order
- Mark the begining of each level and compare current node value with previous value and return false if conditions fail
- Initalize previous value to -inf if level is even and inf if level is odd (when level is even we need ascending order => prev should always be lesser than current, similarly for odd levels)