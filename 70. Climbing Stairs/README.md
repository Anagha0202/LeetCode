#70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

#Solution approach:

DFS = O(2^n)
DP = O(n) => memoization

1D- DP and recursion: So there's 2 ways you can go at each step. 
Base condition:
If it goes beyond n then return 0. 
If its at n then theres only one way to reach nth step so return 1.
If its already present in the dp then take it directly

It will go like depth first search so call it each time with 2 cases: +1 step and +2 steps
and save the value [i] in dp at each calculation ending.