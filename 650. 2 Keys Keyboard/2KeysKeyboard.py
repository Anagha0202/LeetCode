class Solution:
    def minSteps(self, n: int) -> int:
        # if n=2: 1 Copy, 1 Paste = 2 moves
        # if n=3: 1 Copy, 1 Paste, 1 Paste = 3 moves
        # if n=4: (1 Copy, 1 Paste, 1 Paste, 1 Paste) OR (1 Copy, 1 Paste, 1 Copy, 1 Paste) =>  factors(4) = ((2,2),(4,1)) => min((n=2+n=2),) [Ignore n=1 and n=n] => 4 moves
        # if n=5: factors(5) = () => prime number so n moves => 5 moves
        # if n=6: factors(6) = ((2,3),(3,2)) => min((n=2+n=3),(n=3+n=2)) => 5 moves
        #         [(1 Copy, 1 Paste, 1 Copy, 1 Paste, 1 Paste) OR (1 Copy, 1 Paste, 1 Paste, 1 Copy, 1 Paste)]
        # For each n, it ultimately consists of either (n=2) moves or (n=3) moves or a combination of both

        # Approach 2:
        if n<2:
            return 0
        div = 2
        moves = 0
        while n>=2:
            while n%div==0:
                moves+=div
                n/=div
            div+=1
        return moves



        # Approach 1:
        # Time: O(n^2 * sqrt(n))
        # Space: O(n+1)
        if n<2:
            return 0
        dp = [-1]*(n+1)
        dp[0], dp[1] = 0, 0

        def factors(num):
            factors = set()
            for i in range(2, num):
                if num%i==0:
                    factors.add((i,num//i))
            return factors

        def helper(num):
            if dp[num]!=-1:
                return dp[num]
            if num<=3:
                return num
            moves = float("inf")
            f = factors(num)
            for f1,f2 in f:
                moves = min(moves, helper(f1)+helper(f2))
            dp[num] = moves if f else num
            return dp[num]
        
        return helper(n)