# 155. Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.

Approach:
-maintain a minstack within the class 
-minstack keeps track of the min value in the stack at each node
-on popping a value from the stack, pop it from minstack so that the next getMin operation will return the corresponding min value.