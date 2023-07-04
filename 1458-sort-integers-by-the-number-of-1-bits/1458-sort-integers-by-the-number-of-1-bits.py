class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:        
        heap = []

        for n in arr:
            ones = bin(n).count("1")
            heapq.heappush(heap, (ones, n))

        res = []
        while heap: 
            ones, n = heapq.heappop(heap)
            res.append(n)
        return res