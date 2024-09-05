class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #Bottom Up
        # t: O(amount*len(coins))
        # s: O(amount)
        # coins = [1,3,4,5]
        # amount = 7
        dp = [math.inf]*(amount+1) #[0,1,2,1,inf,inf,inf,inf]
        dp[0] = 0
        for amt in range(1, amount+1): # 1,2,3
            print("amt=", amt)
            for coin in coins: # 1,3,4,5
                temp_amt = amt - coin # 0
                if temp_amt>=0:
                    dp[amt] = min(dp[amt], 1 + dp[temp_amt])
        
        return dp[amount] if dp[amount]<math.inf else -1