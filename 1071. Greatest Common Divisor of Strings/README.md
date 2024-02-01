# 1071. Greatest Common Divisor of Strings
Easy

For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

# Approach 
- Greedy approach to loop over the smallest of str1 and str2 because if x is not a divisor of the smaller string then no need to check the larger one
- Take a substring of max length, using that substring create a string of length str1 and string of length str2 to compare with original strings. 

Time: O(min(n,m).(m+n)) [min(n,m)->loop over smallest one, (m+n)->each time we create both strings]