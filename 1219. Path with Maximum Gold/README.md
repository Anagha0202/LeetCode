# 1219. Path with Maximum Gold

Medium

In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position, you can walk one step to the left, right, up, or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.

# Approach
- recursively collect gold from each cell and track the cells that are already visited.
- breaking condition : cell contains 0, going outside the grid, previsiously visited cell 
- at each cell find the maximum gold that can be collected from going all 4 directions from that cell 

# Note: 
Python is interpreted language => code is processed at runtime => parameters can be sent via pass by value or reference (decided by interpreter) does not delete recrusively passed variables after exiting the scope => consistency of parameter values between recursive calls needs to be manually maintained