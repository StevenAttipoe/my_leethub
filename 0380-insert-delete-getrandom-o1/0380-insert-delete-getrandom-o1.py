class RandomizedSet:

    def __init__(self):
        self.nums = {}
        self.numsList = []

    def insert(self, val: int) -> bool:
        isAbsent =  val not in self.nums

        if isAbsent:
            self.nums[val] = len(self.numsList)
            self.numsList.append(val)
            return True
        
        return False
        

    def remove(self, val: int) -> bool:
        isPresent =  val in self.nums
        
        if isPresent:
            idx = self.nums[val]
            lastNum = self.numsList[-1]
            self.numsList[idx] = lastNum
            self.numsList.pop()
            self.nums[lastNum] = idx
            del self.nums[val]
            return True
        
        return False
        

    def getRandom(self) -> int:
        return self.numsList[random.randint(0, len(self.numsList) - 1)]

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()