# 2191. Sort the Jumbled Numbers
Medium
Topics: Arrays, Sorting
Companies: Goldman Sachs
Data Structure: Priority Queue (Heap)

You are given a 0-indexed integer array mapping which represents the mapping rule of a shuffled decimal system. mapping[i] = j means digit i should be mapped to digit j in this system.

The mapped value of an integer is the new integer obtained by replacing each occurrence of digit i in the integer with mapping[i] for all 0 <= i <= 9.

You are also given another integer array nums. Return the array nums sorted in non-decreasing order based on the mapped values of its elements.

Notes:

Elements with the same mapped values should appear in the same relative order as in the input.
The elements of nums should only be sorted based on their mapped values and not be replaced by them.

# Approach:
- Heap sort to sort the numbers based on their mapped values and their index in the input array 
- can conver input to string and then map to respective values in mapping OR
- do conversions digit wise