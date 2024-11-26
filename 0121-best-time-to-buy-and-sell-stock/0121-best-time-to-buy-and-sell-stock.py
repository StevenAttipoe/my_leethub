class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = math.inf

        for p in prices:
            minPrice = min(p, minPrice)
            maxProfit = max(maxProfit, p - minPrice)
        
        return maxProfit