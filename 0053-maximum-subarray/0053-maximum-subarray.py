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

    def maxSubArray2(self, nums):
        dp = [0]*len(nums)
        for i,num in enumerate(nums):            
            dp[i] = max(dp[i-1] + num, num)
        return max(dp)
        