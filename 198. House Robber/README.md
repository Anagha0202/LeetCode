# 198. House Robber
Medium
Topics: DP
Companies: Google
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

# Approach
- Start from reverse order
- Rob last house or rob its next house
- in bottom up: robbing a house = max(robbing this house+robbing house+2, robbing house+1)
- in top down: robbing a house = max(robbing this house+recursive(robbing house-2), recursive(robbing house-1))