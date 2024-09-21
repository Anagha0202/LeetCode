# Binary Search Tree 
class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None

class MyCalendar:

    def __init__(self):
        self.root = None

    def insert(self, start, end, node):
        if start>=node.end:
            if node.right:
                return self.insert(start, end, node.right)
            else:
                node.right = Node(start,end)
                return True
        elif end<=node.start:
            if node.left:
                return self.insert(start,end,node.left)
            else:
                node.left = Node(start, end)
                return True
        else:
            return False

    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root = Node(start,end)
            return True
        else:
            return self.insert(start, end, self.root)


# Using List and Binary Search
class MyCalendar:

    def __init__(self):
        self.books = []

    def lower_binary_search(self, nums, target):
        low, high = 0, len(nums)-1
        while low<=high:
            mid = low + (high-low)//2
            if target<=nums[mid][0]:
                high = mid-1
            else:
                low = mid+1
        return low

    def book(self, start: int, end: int) -> bool:
        index = self.lower_binary_search(self.books, start)
        if (index>0 and self.books[index-1][1]>start) or (index<len(self.books) and end>self.books[index][0]):
            return False
        self.books.insert(index, (start,end))
        return True

# Using SortedList and Bisect
from sortedcontainers import SortedList
class MyCalendar:

    def __init__(self):
        self.books = SortedList([(-math.inf, -math.inf), (math.inf, math.inf)])

    def book(self, start: int, end: int) -> bool:
        index = self.books.bisect_left((start,end))
        if start<self.books[index-1][1] or end>self.books[index][0]:
            return False
        self.books.add((start,end))
        return True
