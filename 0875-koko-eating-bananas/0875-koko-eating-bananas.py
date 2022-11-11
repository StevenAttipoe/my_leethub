class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = float("inf")
        
        left, right = 1, max(piles)
        while left<=right:
            mid = (left + right) // 2
            currTime = 0
            for num in piles:
                if mid >= num:
                    currTime += 1
                else:
                    currTime += math.ceil(num/mid)

            if currTime <= h:
                k = min(k,mid)
                right = mid - 1
                
            else:
                left = mid + 1
            
        return k
            