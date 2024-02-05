# 387. First Unique Character in a String

Easy

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

# Approach
- Keeping track of the count of characters will give the characters that are present only once. 
- Since we go through the string from beginning to end while creating the dictionary, the first character in the dict that has a count of 1 will be the result character.
- Find the index of the result character 