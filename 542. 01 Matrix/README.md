# 542. 01 Matrix
Medium
Companies : Amazon, Google, ByteDance

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

# Approach
- Start from the 0's and expand inwards till the 1's with the maximum distance
- Mark all the non-zero cells as unseen and starting from a zero cell in the queue, move to the nearest unseen cell (which will have a 1)
- BFS