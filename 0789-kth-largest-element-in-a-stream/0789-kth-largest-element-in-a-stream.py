class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.stream = nums 
        self.k = k
        while len(self.stream) > k:
            heapq.heappop(self.stream)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.stream, val)

        while len(self.stream) > self.k:
            heapq.heappop(self.stream)
            
        return self.stream[0] if len(self.stream) else -1

        

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)