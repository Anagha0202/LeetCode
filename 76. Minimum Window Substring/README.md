# 76. Minimum Window Substring

Hard

Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

# Approach: 
Take a window of characters from i to j 
    If need character is found:
        update have dict, 
        if count is exactly what is in need dict:
            update have count
    move j forward and repeat until substring is found. 
    store the indexes and length
Move i forward until have count < need count i.e window fails
    => then move j forward and repeat