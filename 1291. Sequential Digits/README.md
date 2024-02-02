# 1291. Sequential Digits

Medium

An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

# Approach
- No matter the length of the number it will always contain the same digits in this order "123456789" hence assumed
- Based on this string, extract specific lengths from the string and check that its within the bounds of low and high
- To extract loop starting from len of low and go upto len of high