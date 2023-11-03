class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int: # O(N log N) time & O(N) space
        points = defaultdict(int)

        for n in nums:
            points[n] += n

        sorted_nums = sorted(points.keys())
        first = 0
        second = points[sorted_nums[0]]

        for i in range(1, len(sorted_nums)):
            cur = sorted_nums[i]

            if cur == sorted_nums[i - 1] + 1:
                first, second = second, max(second, first + points[cur])
            else:
                first, second = second, second + points[cur]

        return second

    def deleteAndEarn2(self, nums: List[int]) -> int: # O(N + K) time & O(N) space
        points = {}
        high = 0

        for n in nums:
            points[n] = points.get(n, 0) + n
            high = max(high, n)

        first = 0
        second = points.get(1, 0)

        for i in range(2, high + 1):
            cur = max(second, first + points.get(i, 0))
            first = second
            second = cur

        return second

    def deleteAndEarn3(self, nums: List[int]) -> int: # O(N + K) time & O(N + K) space
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
        