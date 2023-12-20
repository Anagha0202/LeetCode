import heapq
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        # Solution 2:
        heapq.heapify(prices)
        diff = money - (heapq.heappop(prices) + heapq.heappop(prices))
        return diff if diff>=0 else money

        # Solution 1:
        prices.sort()
        return money-(prices[0]+prices[1]) if money-(prices[0]+prices[1]) >= 0 else money