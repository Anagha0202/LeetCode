# 279. Perfect Squares

Medium

Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

# Approach:
- if n= 12, if you start from a sum=0 and add 1^2, sum becomes 1. Is the same as saying n is updated to n=11. 
- so (1^2 + no of squares for n=11) is equal to  n=12
- Hence its clearly DP and because we need the value of n=11 in order to find n=12, Bottom up approach