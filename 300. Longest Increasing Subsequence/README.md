# 300. Longest Increasing Subsequence
Medium
Topics: DP
Companies: Google
Given an integer array nums, return the length of the longest strictly increasing subsequence.

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

# Approach
- DP bottom up 
- given [1,2,3] => cache[2] = 1 longest subsequence starting at index 2 can only be 1
- using previous cache values, find longest subsequence starting at each index 
- at each index have to consider all elements on the right 
- return the max of the cache
- Greedy + Binary Search 
- Keeping adding to subsequence until number becomes greater than the last num in subsequence
- Find index of first element >= num and replace num into the subsequence at that index. This ensures that the lenght of subsequence remains same. 
- return the length of the subsequence