# 509. Fibonacci Number

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.

Given n, calculate F(n).

Approach:
-DP
-using DFS at each stage, 2 branches, n-1 and n-2
-add both branches to make final solution
-Base case: when n<=0 => 0
            when n==1 => 1
            when n in dp => dp[n]