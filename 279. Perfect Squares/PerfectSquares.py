class Solution:
    def numSquares(self, n: int) -> int:
        # Not Greedy:
        # Example: n=12
        # Considering initial sum=0 and greedy method we would take 3^2 => n = 3
        # To cover 3 => 1+1+1 So will take 4 perfect squares. Which is wrong

        # We have to consider all possibilities => DP

        # Bottom up approach

        dp = [n] *(n+1) # if 1 is added each time, then height of the tree will be n so max at each n value is n
        dp[0] = 0 # number of squares needed to reach 0 is 0

        for target in range(1, n+1):
            for s in range(1, target+1):
                if target-(s*s) < 0:
                    break
                dp[target] = min(dp[target], 1+dp[target-(s*s)])
        return dp[n]