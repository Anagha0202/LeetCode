# 792. Number of Matching Subsequences

Medium
Topics: Buckets
Companies: Google
Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
 
Example 1:

Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".

# Approach:
- Basic Brute Force:
- compare each word in words with s and find if it is a subsequence using greedy two pointer method and return the largest word
- A bit optimized Brute Force:
- Max heap to provide the longest strings first and greedily check if subsequence 
- t: O(n*m)
- s: O(n)

- Procesing by Buckets
- approach is to compare a character in s, s[i] with character present at i all words. 
- Preprocess words based on the first character which gives dictionary where words are sorted based on first character and the first character is the key. 
- Iterate over S. for each character s[i] process word dict[s[i]] and remove the first character from all the words and regroup based on the current first character. This means that first character in all those words has been found in S hence until that index, the word can be made. 
- When the word is emptied i.e. removing the first characters led to empty string, => word has been found and count can be incremented
- t: O(n+m) 
- s: O(m)