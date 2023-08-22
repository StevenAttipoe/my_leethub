class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        lastStone = 0

        while len(stones) > 1:
            stones.sort()
            x, y = stones[-2], stones[-1]

            if x == y:
                stones.pop()
                stones.pop()

            else:
                stones.pop(-2)
                stones[-1] = y - x

        return stones[0] if len(stones) else 0
