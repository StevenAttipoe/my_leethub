class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        runningSum = 0
        
        for n in nums:
            runningSum += n
            res = max(res, runningSum)
            if runningSum < 0:
                runningSum = 0
                
        return res
        