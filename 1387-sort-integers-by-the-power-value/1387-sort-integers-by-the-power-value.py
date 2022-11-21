class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        res = []

        for num in range(lo, hi + 1):
            res.append([num, self.getSteps(num)])

        res.sort(key= lambda x:x[1])

        return res[k-1][0]
        
        
    def getSteps(self,num):
        steps = 0
        while (num != 1 and num > 0):
            if num % 2 == 0:
                num = num // 2
            elif num % 2 != 0:
                num = 3 * num + 1
            steps += 1
        return steps
        