# 729. My Calendar I
Medium
Topics: Binary Search Tree BST, Binary Search, SortedList
Companies: Google
You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendar class:

MyCalendar() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.
 
Example 1:
Input
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
Output
[null, true, false, true]

Explanation
MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.

# Approach:
- node consists of start and end time of event
- Build BST such that all events with start and end times before the root are on left subtree and all events with start and end times after the root are on right subtree
- Build tree recursively
- if start time is after end time of root node, move to right branch if exists
- else if end time is before starttime of root node, move to left branch if exists
- if event start and end times are overlapping with another events start or end time, return False