class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = {}
        high = 0

        for n in nums:
            points[n] = points.get(n, 0) + n
            high = max(high, n)

        dp = [0] * (high + 1)
        dp[1] = points.get(1, 0)

        for i in range(2, high + 1):
            dp[i] = max(dp[i -  1], dp[i - 2] + points.get(i, 0))

        return dp[-1]
        