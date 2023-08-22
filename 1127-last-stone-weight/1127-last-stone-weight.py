class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        print(stones)

        while len(stones) > 1:
            y, x = heapq.nsmallest(2, stones)

            heapq.heappop(stones)
            heapq.heappop(stones)

            print(x, y, -(abs(y) - abs(x)))

            if x != y:
                heapq.heappush(stones, -(abs(y) - abs(x)))
        
        return -stones[0] if len(stones) else 0
