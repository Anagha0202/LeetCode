# 238. Product of Array Except Self

Medium

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

# Approach:
- Main clue is the mention of prefix and suffix
- result of any item is the product of the items before it and after it => prefix and suffix product of each item is needed
- calculate the prefix upto an item not including
- calculate the suffix upto an item starting from the right side of list not including the item
- final result found by product of the prefix and suffixes of each item