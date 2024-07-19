# 1380. Lucky Numbers in a Matrix
Easy
Topics: Array, Matrix
Companies: Apple

Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

# Approach:
- traverse matrix, at each element check if its minimum of the row maintained in mins[i] and check if it is the maximum element in col maintained by maxs[j]
- intersection between the 2 gives the Lucky Number that is min in row and max in col