513. Find Bottom Left Tree Value

Medium

Given the root of a binary tree, return the leftmost value in the last row of the tree.

# Approach 
- The tree and the need to traverse down to the bottom level implies either DFS or BFS. 
- Traversing the tree BFS or level wise will allow us to mark the first value at each level and traverse down the tree until no new levels are found and we can return the last found value. 
- At each level, mark the first node, then traverse all the nodes in that level (traverse queue.length) and simulataneously add the branches to the queue. But traverse its branches in the next round. 