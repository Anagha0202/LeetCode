class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        diff = [[0]*cols for _ in range(rows)]

        # Solution 2:
        # Time: O(n*m)    Space: O(n*m)
        rowSum, colSum = [0]*rows, [0]*cols
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    rowSum[i] += 1
                    colSum[j] += 1
                else:
                    rowSum[i] -= 1
                    colSum[j] -= 1

        for i in range(rows):
            for j in range(cols):
                diff[i][j] = rowSum[i] + colSum[j]
        
        # print(diff)
        return diff
    
        # Solution 1:
        # row wise 1's and 0's calculations 
        for i in range(rows):
            rowSum = 0
            for j in range(cols):
                if grid[i][j] == 1:
                    rowSum += 1
                else:
                    rowSum -= 1
            diff[i] = [rowSum]*cols

        # column wise 1's and 0' calculation combined with row calc 
        for j in range(cols):
            colSum = 0
            for i in range(rows):
                if grid[i][j] == 1:
                    colSum += 1
                else:
                    colSum -= 1
            
            for i in range(rows):
                diff[i][j] += colSum
        
        # print(diff)

        return diff