# 149. Max Points on a Line
Hard
Topics: Hashmap
Companies: Google, Amazon, Linkedin, Oracle
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

Example 1:
Input: points = [[1,1],[2,2],[3,3]]
Output: 3

# Approach
- use one point as the common point that all lines will pass through 
- calculate slopes of each point using the common point 
- reduce each slope (y,x) pair by gcd(x,y) to bring it to lowest value to compare with other slopes
- group into dict based on slope values and find maximum points on the same slope