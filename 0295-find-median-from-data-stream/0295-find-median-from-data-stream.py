class MedianFinder:

    def __init__(self):
        self.maxHeapForMinVals = []
        self.minHeapForMaxVals = []

    def addNum(self, num: int) -> None:
        heappush(self.maxHeapForMinVals, -num)
        heappush(self.minHeapForMaxVals, -self.maxHeapForMinVals[0])
        heappop(self.maxHeapForMinVals)

        if len(self.maxHeapForMinVals) < len(self.minHeapForMaxVals):
            heappush(self.maxHeapForMinVals, -self.minHeapForMaxVals[0])
            heappop(self.minHeapForMaxVals)

    def findMedian(self) -> float:
        if len(self.maxHeapForMinVals) > len(self.minHeapForMaxVals):
            return -1.0 * self.maxHeapForMinVals[0]
        
        return (self.minHeapForMaxVals[0] - self.maxHeapForMinVals[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()