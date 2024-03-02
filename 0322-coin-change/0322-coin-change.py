class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        N = amount + 1
        dp = [N] * N
        dp[0] = 0

        for a in range(1, N):
            for c in coins:
                if c <= a:
                    change = a - c
                    dp[a] = min(dp[a], 1 + dp[change])

        return dp[-1] if dp[-1] != N else -1
        