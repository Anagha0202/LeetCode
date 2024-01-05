# 2870. Minimum Number of Operations to Make Array Empty
Medium

You are given a 0-indexed array nums consisting of positive integers.

There are two types of operations that you can apply on the array any number of times:

Choose two elements with equal values and delete them from the array.
Choose three elements with equal values and delete them from the array.
Return the minimum number of operations required to make the array empty, or -1 if it is not possible.

# Approach:
We only need to count the operations. 
Creating triplets rather than pairs will always lead to smaller number of operations. 
Only 2 major cases :    if count of number is 1 => return -1
                        else count is not 1
                            2 options:  count is multiple of 3 => create all triplets
                                        count is not multiple of 3 => create all possible triplets and add 1 for any remainders