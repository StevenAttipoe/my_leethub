class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:        
        heap = []

        for n in arr:
            ones = self.countOnes(n)
            heapq.heappush(heap, (ones, n))

        res = []
        while heap: 
            ones, n = heapq.heappop(heap)
            res.append(n)
        return res

    def countOnes(self, n):
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count