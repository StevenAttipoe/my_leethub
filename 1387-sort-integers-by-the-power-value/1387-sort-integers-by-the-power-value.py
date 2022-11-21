class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        res = []

        for num in range(lo, hi + 1):
            res.append([num, self.getSteps(num)])

        res.sort(key= lambda x:x[1])

        return res[k-1][0]
        
        
    def getSteps(self,num, memo = {1:0}):
        steps = 0
        while (num != 1 and num > 0):
            old = num
            if num in memo:
                num = memo[num]
                steps += 1
                continue
            elif num % 2 == 0:
                num = num // 2
            else:
                num = 3 * num + 1
            memo[old] = num
            steps += 1
        return steps
        