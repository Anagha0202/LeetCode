# 3005. Count Elements With Maximum Frequency

Easy

You are given an array nums consisting of positive integers.

Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

The frequency of an element is the number of occurrences of that element in the array.

# Approach
- One way is to find counts of all elemments in a dictionary, take the max count and add the element counts that match the max count
- One pass solution is in one pass identify the current max count and the number of elements that match the max count until now. Update the max count if the count increases and same time update the count of elements that match the count.