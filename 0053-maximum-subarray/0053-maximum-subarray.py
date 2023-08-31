class Solution:
    def maxSubArray2(self, nums: List[int]) -> int:
        res = nums[0]
        runningSum = 0
        
        for n in nums:
            runningSum += n
            res = max(res, runningSum)
            if runningSum < 0:
                runningSum = 0
                
        return res

    def maxSubArray(self, nums):
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]

        for i in range(1, n): 
            num = nums[i]           
            dp[i] = max(dp[i - 1] + num, num)

        return max(dp)
        