class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        edges cases:
        if only one house: money
        if only 2 houses: return max money

        Brute Force:
        start at each house, rob it, move to house+2 and calculate the total robbed amount.
        take maximum of ribbed amount
        t: O(n^2)
        s: O(1)

        robbing a house depends on the maximum you can get by robbing the house-2

        Bottom up DP: iterative
        at each house, we can rob either house or house+1, which ever is greater
        in dp we are trackign the max that can be robbed until each house
        if house+2 is also valid, then at current house, maximum robbed will be max(robbing this house+dp[house+2] or dp[house+1])
        t: O(n)
        s: O(n)

        we rob house n-1, move ahead by house+2 which will be invalid so we add 0 to robbed
        we rob house n-2, move ahead by house+2 which will be invalid so we add 0 to robbed
        we rob house n-3, move ahead by house+2, house+1 if valid -> 
            +2 give n-1 which we have already robbed before and know the maximum amout we can get by robbing n-1 -> add that to current robbed amount
            +1 gives n-2 which we hav already robbed -> robbed[n-2]
        take max of robbing this house and house+2 and not robbing this house and robbing house+1
        at each house track the max robbed in dp array

        Top down DP: recursion
        at a house, we can either rob it, or not rob it and move to the next house. 
        At house n, we can rob it and move it house n-12 or not rob it and move to house n-1
        when we go beyond the houses, return 0
        if not, return money of  max (that house + ahead, or house+1)
        t: O(n)
        s: O(n)
        """
        if len(nums)==1:
            return nums[0]
        if len(nums)<=2:
            return max(nums)

        # Bottom UP
        def bottom_up(nums):
            robbed = [0]*(len(nums)+1)
            for house in range(len(nums)-1, -1, -1):
                robbed[house] = nums[house]
                if house+2 < len(nums):
                    robbed[house] = max(robbed[house]+robbed[house+2], robbed[house+1])
                elif house+1 < len(nums):
                    robbed[house] = max(robbed[house], robbed[house+1])
                # print(robbed)
                
            return robbed[0]
        
        robbed = [-1]*(len(nums)+1)
        def top_down(house):
            # print(house)
            if house<0:
                return 0
            if robbed[house]!=-1:
                return robbed[house]
            robbed[house] = max(nums[house]+top_down(house-2), top_down(house-1))
            return robbed[house]
        
        return top_down(len(nums)-1)