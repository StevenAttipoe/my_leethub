class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i, stone in enumerate(stones):
            stones[i] = -stone

        heapq.heapify(stones)

        while len(stones) > 1:
            y, x = heapq.nsmallest(2, stones)

            heapq.heappop(stones)
            heapq.heappop(stones)

            if x != y:
                heapq.heappush(stones, -(abs(y) - abs(x)))
        
        return -stones[0] if len(stones) else 0
