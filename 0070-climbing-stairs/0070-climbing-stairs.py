class Solution:
    def climbStairs2(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[-1]

    def climbStairs(self, n: int) -> int:
        memo = [0] * (n + 1)
        return self.takeSteps(0, n, memo)
    
    def takeSteps(self, step, n, memo):
        if step > n:
            return 0
        if step == n:
            return 1
        if memo[step] > 0:
            return memo[step]

        memo[step] = self.takeSteps(step + 1, n, memo) + self.takeSteps(step + 2, n, memo)
        return memo[step]