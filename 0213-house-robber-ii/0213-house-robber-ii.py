class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        
        def helper(nums):
            first= nums[0]
            second = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                cur = max(second, nums[i] + first)
                first = second
                second = cur
            
            return second

        return max(helper(nums[:-1]), helper(nums[1:]))

    def rob2(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        
        def helper(nums):
            n = len(nums)
            dp = [0] * n
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, n):
                dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
            
            return dp[-1]

        return max(helper(nums[:-1]), helper(nums[1:]))