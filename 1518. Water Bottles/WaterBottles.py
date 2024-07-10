class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # Approach 2: when 3 (numExchange) bottles are given, you get back 1.
        # Which means 3-1 (numExchange-1) bottles are given away each time. 
        # You are guaranteed to get back one bottle each time which means that 
        # you are exchanging 9-1 (numBottles-1) bottles only. 
        # Time: O(1)
        # Space: O(1)

        return numBottles + (numBottles-1)//(numExchange-1)

        # Approach 1: In each round, 9/3 (numBottles/numExchange) is exchanged for 
        # filled bottles. The number of bottles remaining after the exchange is the 
        # number of bottles got after exchange + any bottles remaining that were not 
        # a part of the exchange.
        # Time: O(n)
        # Space: O(1)
        total = numBottles
        while numBottles>=numExchange:
            total+=numBottles//numExchange
            numBottles = (numBottles//numExchange) + (numBottles%numExchange)
        return total