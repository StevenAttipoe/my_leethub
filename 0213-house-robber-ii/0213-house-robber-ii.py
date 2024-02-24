class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)

        if N == 1: return nums[0]
        if N == 2: return max(nums)

        def calcMaxRob(nums):
            oneBack = twoBack = 0
            for n in nums:
                maxRob = max(oneBack, n + twoBack)
                twoBack = oneBack
                oneBack = maxRob
            
            return maxRob

        return max(calcMaxRob(nums[:-1]), calcMaxRob(nums[1:]))

    def rob2(self, nums: List[int]) -> int:
        N = len(nums)

        if N == 1: return nums[0]
        if N == 2: return max(nums)

        def calcMaxRob(nums, N):
            dp = [0] * N
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, N):
                dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
            
            return dp[-1]

        return max(calcMaxRob(nums[:-1], N - 1), calcMaxRob(nums[1:], N - 1))