class Solution:
    def isHappy(self, n: int) -> bool:
        
        def getNext(n):
            totalSum = 0
            while n != 0:
                lasNum = n % 10
                n = n // 10
                totalSum += lasNum ** 2
            return totalSum
        
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = getNext(n)
            
        return n == 1
            
            