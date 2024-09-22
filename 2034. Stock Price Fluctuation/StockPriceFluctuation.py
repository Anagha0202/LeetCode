class StockPrice:

    def __init__(self):
        self.timestamp_price = collections.defaultdict(int)
        self.recent_timestamp = 0
        self.current_price = 0
        self.max_heap = []
        self.min_heap = []

    def update(self, timestamp: int, price: int) -> None:
        self.timestamp_price[timestamp] = price
        # print("timestamp_price:", self.timestamp_price)
        heapq.heappush(self.max_heap, (-price, timestamp))
        heapq.heappush(self.min_heap, (price, timestamp))
        if timestamp>=self.recent_timestamp:
            self.current_price = price
            self.recent_timestamp = timestamp

    def current(self) -> int:
        return self.current_price

    def maximum(self) -> int:
        while self.timestamp_price[self.max_heap[0][1]] != -self.max_heap[0][0]:
            heapq.heappop(self.max_heap)
        return -self.max_heap[0][0] #only return value without removing the max from the heap as removing would alter future values

    def minimum(self) -> int:
        while self.timestamp_price[self.min_heap[0][1]] != self.min_heap[0][0]:
            heapq.heappop(self.min_heap)
        return self.min_heap[0][0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()