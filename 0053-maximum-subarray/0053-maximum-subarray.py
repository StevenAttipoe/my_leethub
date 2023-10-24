class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_subarray = max_subarray = nums[0]
        
        for num in nums[1:]:
            current_subarray = max(num, current_subarray + num)
            max_subarray = max(max_subarray, current_subarray)
        
        return max_subarray

    def maxSubArray2(self, nums):
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]

        for i in range(1, n): 
            num = nums[i]           
            dp[i] = max(dp[i - 1] + num, num)

        return max(dp)

    def maxSubArray3(self, nums: List[int]) -> int:
        res = nums[0]
        runningSum = 0
        
        for n in nums:
            runningSum += n
            res = max(res, runningSum)
            if runningSum < 0:
                runningSum = 0
                
        return res
        