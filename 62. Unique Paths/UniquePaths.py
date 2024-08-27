class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # DP-tabulation
        # t: O(m*n)
        # s: O(m*n)
        # dp stores the no of ways to reach the current cell from beginning (0,0)
        dp = [[1]*n for _ in range(m)]
        def tabulation(m, n):
            for i in range(1,m):
                for j in range(1,n):
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
            return dp[m-1][n-1]


        # DP-memoization
        # t: O(m*n)
        # s: O(m*n)
        # dp stores no of ways to reach destination (rows-1,cols-1) from current cell
        # dp = {}
        def dfs(i, j, rows, cols):
            if i>=rows or j>=cols:
                return -1
            if i==rows-1 and j==cols-1:
                return 1
            if (i,j) in dp:
                return dp[(i,j)]
            
            right = dfs(i, j+1, rows, cols)
            right = right if right>0 else 0
            down = dfs(i+1, j, rows, cols)
            down = down if down>0 else 0

            dp[(i,j)] = right+down
            return dp[(i,j)]

        # return dfs(0,0,m,n)
        return tabulation(m,n)