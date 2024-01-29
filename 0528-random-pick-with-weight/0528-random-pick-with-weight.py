class Solution:

    def __init__(self, w: List[int]):
        self.runningSums = []
        self.cumulativeSum = 0

        for weight in w:
            self.cumulativeSum += weight
            self.runningSums.append(self.cumulativeSum)

    def pickIndex(self) -> int:
        randomWeight = self.cumulativeSum * random.random()

        for index, runningSum in enumerate(self.runningSums):
            if runningSum > randomWeight:
                return index


        

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()