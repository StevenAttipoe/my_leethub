class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        for i in range(N):
            for j in range(i + 1, N):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        return [-1, -1]
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}

        for i, n in enumerate(nums):
            numsMap[n] = i
        
        for i, n in enumerate(nums):
            dif = target - n
            if dif in numsMap and numsMap[dif] != i:
                return [i, numsMap[dif]]
        
        return [-1, -1]
        