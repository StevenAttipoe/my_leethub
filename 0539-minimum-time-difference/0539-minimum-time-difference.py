class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        M = 1440
        day = [None] * 1440

        for time in timePoints:
            minute = self.getMinutes(time)
            if day[minute]:
                return 0
            day[minute] = True
        
        minutes = [i for i in range(M) if day[i]]

        minDiff = float('inf')
        for i in range(len(minutes)):
            minDiff = min(minDiff, (minutes[i] - minutes[i - 1]) % M)

        return minDiff

    def getMinutes(self, time):
        h, m = map(int, time.split(':'))
        return (60 * h) + m
        