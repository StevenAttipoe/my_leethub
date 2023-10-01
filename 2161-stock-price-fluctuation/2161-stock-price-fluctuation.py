class StockPrice:

    def __init__(self):
        self.timestamps = {}
        self.minHeap = []
        self.maxHeap = []
        self.maxTime = 0
        

    def update(self, timestamp: int, price: int) -> None:
        self.timestamps[timestamp] = price
        self.maxTime = max(self.maxTime, timestamp)

        heappush(self.minHeap, (price, timestamp))
        heappush(self.maxHeap, (-price, timestamp))

    def current(self) -> int:
        return self.timestamps[self.maxTime]

    def maximum(self) -> int:
        curPrice, time = heappop(self.maxHeap)

        while -curPrice != self.timestamps[time]:
            curPrice, time = heappop(self.maxHeap)
        
        heappush(self.maxHeap, (curPrice, time))
        return -curPrice
    def minimum(self) -> int:
        curPrice, time = heappop(self.minHeap)

        while curPrice != self.timestamps[time]:
            curPrice, time = heappop(self.minHeap)
        
        heappush(self.minHeap, (curPrice, time))
        return curPrice
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()