class Solution:
    def __init__(self, w: List[int]):
        self.runningSums = []
        self.cumulativeSum = 0

        for weight in w:
            self.cumulativeSum += weight
            self.runningSums.append(self.cumulativeSum)

    def pickIndex(self) -> int:
        target = random.uniform(0, self.cumulativeSum)
        return self.binarySearch(self.runningSums, target)

    
    def binarySearch(self, runningSums, target) -> int:
        l, r = 0, len(runningSums)

        while l < r:
            mid = (l + r) // 2

            if runningSums[mid] < target:
                l = mid + 1
            else:
                #the search space greater than mid mid but we want the min greatest value
                r = mid
        #return l or r, it doesn't matter
        return r

class Solution2:
    def __init__(self, w: List[int]):
        self.runningSums = []
        self.cumulativeSum = 0

        for weight in w:
            self.cumulativeSum += weight
            self.runningSums.append(self.cumulativeSum)

    def pickIndex(self) -> int:
        target = random.uniform(0, self.cumulativeSum)

        for index, runningSum in enumerate(self.runningSums):
            if runningSum > target:
                return index


        

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()