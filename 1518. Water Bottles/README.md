# 1518. Water Bottles
Easy
Companies : Amazon

There are numBottles water bottles that are initially full of water. You can exchange numExchange empty water bottles from the market with one full water bottle.

The operation of drinking a full water bottle turns it into an empty bottle.

Given the two integers numBottles and numExchange, return the maximum number of water bottles you can drink.

# Approach
- Approach 2: 
- when 3 (numExchange) bottles are given, you get back 1.
- Which means 3-1 (numExchange-1) bottles are given away each time. 
- You are guaranteed to get back one bottle each time which means that you are exchanging 9-1 (numBottles-1) bottles only. 
- Time: O(1)
- Space: O(1)

- Approach 1: In each round, 9/3 (numBottles/numExchange) is exchanged for 
- filled bottles. The number of bottles remaining after the exchange is the number of bottles got after exchange + any bottles remaining that were not a part of the exchange.
- Time: O(n)
- Space: O(1)