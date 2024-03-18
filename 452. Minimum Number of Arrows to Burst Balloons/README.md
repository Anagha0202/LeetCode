# 452. Minimum Number of Arrows to Burst Balloons

Medium

There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

# Approach:
- Based on intuition, the balloons have to be sorted
- When they are sorted by the ending points => it gives a point that is more likely to belong to more than one balloon
- So sorting in ascending order based on the ending point 
- Choosing a value for arrow allows us to determine how many balloons the arrow can go through before needing to change the arrow value
- Choosing the ending value for arrow each time guarantees that this arrow will cover the maximum balloon possible before being out of bounds of the next balloon