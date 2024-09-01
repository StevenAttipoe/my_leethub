class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}            
        
        for i in range(len(nums)):
            dif = target - nums[i]
            
            if dif in numsDict:
                return [i, numsDict[dif]]

            numsDict[nums[i]] = i

                
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}
        
        for i in range(len(nums)):
            numsDict[nums[i]] = i
            
        
        for i in range(len(nums)):
            dif = target - nums[i]
            
            if dif in numsDict and i != numsDict[dif]:
                return [i, numsDict[dif]]
                
        return [-1, -1]