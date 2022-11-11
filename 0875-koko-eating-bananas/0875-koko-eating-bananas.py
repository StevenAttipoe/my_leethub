class Solution:
    #O(log(max(P))*P)
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        minK = max(piles)
        
        while left<=right:
            k = (left + right) // 2
            hours = 0
            for num in piles:
                if k >= num:
                    hours += 1
                else:
                    hours += math.ceil(num/k)

            if hours <= h:
                minK = min(minK,k)
                right = k - 1
                
            else:
                left = k + 1
            
        return minK
            