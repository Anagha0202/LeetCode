# 525. Contiguous Array

Medium

Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

# Approach
- the key point is to find the count starting from the middle of the list
- The last time we encountered the same count will the starting point of the list (not including) until current position from where the count of 1's and 0's will be equal