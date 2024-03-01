# 2864. Maximum Odd Binary Number

Easy

You are given a binary string s that contains at least one '1'.

You have to rearrange the bits in such a way that the resulting binary number is the maximum odd binary number that can be created from this combination.

Return a string representing the maximum odd binary number that can be created from the given combination.

Note that the resulting string can have leading zeros.

# Approach
- Using the odd and even rules, odd+even will always result in odd, and 1 is only odd number in the binary representation. (2,4,8... are all even)
- Greedily we can assume that one count of the available 1's will be placed in the 2^0 position. 
- Remaining counts are greedily placed from the beginning of the string to get the maximum value
- adding any of the even values (2^1, 2^2, ...) with odd value (2^0) will always result in an odd number and will have maximum value as the beginning bits are set. 