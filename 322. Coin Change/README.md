# 322. Coin Change
Medium
Topics: DP
Companies: Facebook
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

# Approach:
- DFS + Backtracking with memoization => Top down
- Interative from 0 to amount => Bottom up 
- choosing a coin depends on the amt available
- if coins = [1,2] and amount = 0 requires 0 coins, amount=1 requires 1 coin, amount = 2 requires 1 coin and amount = 3 requires 2 coins. 
- when amount = 3, if we use coin 1 => new amount = 3-1 = 2 => 1 coin + coins needed for amount 2
                    if we use coin 2 => new amount = 3-2 = 1 => 1 coin + coins needed for amount 1
- trying all posibilities gives us the minimum number of coins for each amount
- using the minimum amount we can calculate the minimum amount for given amount