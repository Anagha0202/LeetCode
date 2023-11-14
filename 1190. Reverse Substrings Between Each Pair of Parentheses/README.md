# 1190. Reverse Substrings Between Each Pair of Parentheses
Medium | 

You are given a string s that consists of lower case English letters and brackets.

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.

Approach:
Track the opening brackets and characters in a stack until a closing bracket is found
on closing bracket, pop from stack into a temp until opening bracket is found
add the popped characters to the stack and continue
