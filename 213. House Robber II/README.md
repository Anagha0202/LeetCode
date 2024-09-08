# 213. House Robber II
Medium
Topics: DP
Companies: Google
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

# Approach
- houses 0 and n-1 are adjacent to each other which means, if we rob house 0, then we cannot rob house n-1 and vice versa. 
- we split the input into 2 houses lists, one having house 0 and one having house n-1