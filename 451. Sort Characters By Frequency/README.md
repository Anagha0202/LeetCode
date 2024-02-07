# 451. Sort Characters By Frequency

Medium

Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

# Approach:
- 1. Using dictionary of counts of characters, sort it based on value in descending order, build string based on key*value
- 2. Use dictionary to save counts of characters, build  max heap (value, key), popping from the heap will return max count characters and can cuild string from that. 

- Time Complexity: O(n)
- Space Complexity: O(n)