# 1513. Number of Substrings With Only 1s

Medium

Given a binary string s, return the number of substrings with all characters 1's. Since the answer may be too large, return it modulo 109 + 7.

# Approach:
- count counts the number of consecutive 1's
- total counts the substrings possible
- when a 0 is encountered, the count is reset as it breaks the consecutive 1's possible