# 2849. Determine if a Cell Is Reachable at a Given Time
Medium | 

You are given four integers sx, sy, fx, fy, and a non-negative integer t.

In an infinite 2D grid, you start at the cell (sx, sy). Each second, you must move to any of its adjacent cells.

Return true if you can reach cell (fx, fy) after exactly t seconds, or false otherwise.

A cell's adjacent cells are the 8 cells around it that share at least one corner with it. You can visit the same cell several times.

Approach:
we don't need the exact path followed so ignore the traversal algos
Since it only requires a true or false, utilise math and calculate the moves required to reach the finish box