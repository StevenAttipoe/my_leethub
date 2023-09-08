class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        step_one = step_two = 0

        for i in range(2, len(cost) + 1):
            cur_step = min(step_one + cost[i - 1], step_two + cost[i - 2])
            step_one, step_two = cur_step, step_one

        return cur_step

    def minCostClimbingStairs2(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)

        for i in range(2, len(cost) + 1):
            take_one_step = dp[i - 1] + cost[i - 1]
            take_two_step = dp[i - 2] + cost[i - 2]
            dp[i] = min(take_one_step, take_two_step)

        return dp[-1]