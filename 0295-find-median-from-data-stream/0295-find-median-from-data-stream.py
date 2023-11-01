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


class MedianFinder2:
    def __init__(self):
        self.stream = []

    def addNum(self, num: int) -> None:
        self.stream.append(num)
        self.stream.sort()
        
    def findMedian(self) -> float:
        n = len(self.stream)
        if n % 2 == 0:
            mid1 = self.stream[((n // 2) - 1)]
            mid2 = self.stream[(n // 2)]
            return (mid1 + mid2) / 2
        
        return self.stream[n // 2]
        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()