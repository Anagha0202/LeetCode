# 1114. Print in Order

Easy

Suppose we have a class:

public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}
The same instance of Foo will be passed to three different threads. Thread A will call first(), thread B will call second(), and thread C will call third(). Design a mechanism and modify the program to ensure that second() is executed after first(), and third() is executed after second().

Note:

We do not know how the threads will be scheduled in the operating system, even though the numbers in the input seem to imply the ordering. The input format you see is mainly to ensure our tests' comprehensiveness.

# Approach:
1. Barriers: 
    - Imagine barrier to be a line that all threads have to reach in order to be released from execution
    - Barrier specifies number of threads it needs to wait for 
    - When threads have called barrier.wait => threads are released
    - In this question, there is a barrier between thread A and thread B and one between thread B and thread C 
    - Once a thread calls first, the barrier is ready to release and after second is called then the barrier is released
    - Similarly for the other barrier between thread B and thread C

2. Locks:
    - locks[0] is between first() and second()
    - locks[1] is between second() and third()
    - initially both are locked 
    - after first is executed, the lock gets released for second to acquire
    - then using 'with' second acquires the lock and releases implicitly
    - second also releases third which is then acquired by third to run the print
    - The next function cannot run until the respective locks are released

3. Events:
    - Event can be set on completion or wait for completion
    - function first completes its task and raises the event[0] implying that event is completed
    - function second waits for first to raise the event[0] and then performs its task. On completing it raises event[1] indicating that event is completed
    - function third waits for event[1] and then performs its task

4. Semaphores:
    - integer object that is shared between threads and works on signaling mechanism.
    - different from mutex because mutex uses locking mechanism and semaphore uses signaling mechanism