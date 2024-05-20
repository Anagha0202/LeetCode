# 979. Distribute Coins in Binary Tree

Medium

You are given the root of a binary tree with n nodes where each node in the tree has node.val coins. There are n coins in total throughout the whole tree.

In one move, we may choose two adjacent nodes and move one coin from one node to another. A move may be from parent to child, or from child to parent.

Return the minimum number of moves required to make every node have exactly one coin.

# Approach
- DFS 
- Return from a child to parent the number of moves required to make the child have exaclty one coin
- Child can return 0 => no move required as it already has a coin
- Child can return -ve => it needs additional coins from parent
- Child can return +ve => it has extra coins that it wants to return to the parent
- Based on child values, parent performs the same calulations as child