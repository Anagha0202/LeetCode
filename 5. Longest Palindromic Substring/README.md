# 5. Longest Palindromic Substring
Medium
Topics: DP
Companies: Google
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

# Approach
- Using 2-D DP to take substrings of len=1,2...
- in a substring, if 2 corner characters are same, being palindrome depends on the substring without first and last character