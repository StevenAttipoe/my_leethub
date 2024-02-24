class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1

        step_zero = step_one = 1

        for _ in range(2, n + 1):
            step_three = step_zero + step_one
            step_zero = step_one
            step_one = step_three

        return step_three

    def climbStairs2(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[-1]

    def climbStairs3(self, n: int) -> int:
        memo = [0] * (n + 1)
        def takeSteps(step, n, memo):
            if step > n:
                return 0
            if step == n:
                return 1
            if memo[step] > 0:
                return memo[step]

            memo[step] = takeSteps(step + 1, n, memo) + takeSteps(step + 2, n, memo)
            return memo[step]
        return takeSteps(0, n, memo)
    
    