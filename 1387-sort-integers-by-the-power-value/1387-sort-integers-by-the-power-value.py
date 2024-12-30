class Solution:
    def getPower(self, x):
        steps = 0

        while x != 1:
            if x % 2 == 0:
                x = x // 2
            else:
                x = 3 * x + 1
            steps += 1
        return steps

    def getPower(self, x, memo, steps):
        if x == 1:
            return steps

        if x % 2 == 0:
            x = x // 2
        else:
            x = 3 * x + 1

        steps += 1
        if x in memo:
            return steps + memo[x]
        
        return self.getPower(x, memo, steps)

    def getKth(self, lo: int, hi: int, k: int) -> int:
        powerVals = {}
        memo = {}

        for i in range(lo, hi + 1):
            p = self.getPower(i,memo, 0)
            memo[i] = p
            powerVals[i] = p
        
        return sorted(powerVals.keys(), key = lambda x: powerVals[x])[k - 1]
        