class Solution:
    def fib(self, n: int) -> int:
        dp = [-1]*(n+1)
        def fibHelper(n, dp):
            if n<=0:
                return 0
            if n==1:
                return 1
            if dp[n]!=-1:
                return dp[n]
            dp[n] = fibHelper(n-1, dp) + fibHelper(n-2, dp)
            return dp[n]
        
        return fibHelper(n, dp)
        