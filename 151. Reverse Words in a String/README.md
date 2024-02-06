# 151. Reverse Words in a String

Medium

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

# Approach
- Pythonic way: strip and split-strip each word in the string and return it joined with a space in reverse order.
- Algorithmic way: Loop character by character, adding a non space character to a temp string until a space is found. On finding a space add the temp string to a list of answers which contains all the words in the string. Join together the words in answer in reverse order with a space in between them and return the final string. 