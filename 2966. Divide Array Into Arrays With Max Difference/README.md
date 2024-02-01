# 2966. Divide Array Into Arrays With Max Difference
Medium

You are given an integer array nums of size n and a positive integer k.

Divide the array into one or more arrays of size 3 satisfying the following conditions:

Each element of nums should be in exactly one array.
The difference between any two elements in one array is less than or equal to k.
Return a 2D array containing all the arrays. If it is impossible to satisfy the conditions, return an empty array. And if there are multiple answers, return any of them.

# Approach 
- Since order of original array does not have to be maintained in order to create the triplets, sort the original array. 
- Take a window of 3 elements, using greedy approach, if ele3-ele1 is greater than k then we can directly return []
- Because the array is sorted and if you consider element at i=0 and element at i=3, the difference will always be greater than that of element at i=0 and element at i=2.