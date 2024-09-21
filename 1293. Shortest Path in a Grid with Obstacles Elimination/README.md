# 1293. Shortest Path in a Grid with Obstacles Elimination
Hard
Topics: BFS
Companies: Google
You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

Example 1:
Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
Output: 6
Explanation: 
The shortest path without eliminating any obstacle is 10.
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).

# Approach 
- BFS to find the shortest path from (0,0) to (n-1,m-1)
- Each box can be reached multiple times so to avoid it use visited set to track the (row,col)
- Each box can be reached from 4 different directions with different vaues for k
- So visited should track row, col with the K value that it has when it reached that box
- increment steps at the end of each round of expansion
- Manhattan distance gives the shortest path to the end and if the number of k > manhattan distance, then all blocks along that path can be removed => manhattan distance will the shortest distance 