class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1]*(n+1)
        def climbStairsHelper(i, n, dp):
            if i>n:
                return 0
            if i==n:
                return 1
            if dp[i]!=-1:
                return dp[i]
            plusone = climbStairsHelper(i+1, n, dp)
            plustwo = climbStairsHelper(i+2, n, dp)

            dp[i] = plusone + plustwo
            return dp[i]
        
        return climbStairsHelper(0, n, dp)
        