# 49. Group Anagrams

Medium

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Approach
- When a string is sorted, its in alphabetical order. 
- If two strings are the same when it is sorted, then it is made up of the same characters => they are anagrams 
- sort each string and add the sorted string as the key of the dict and the corresponding string is the value
- dict.values will give all grouped anagrams.