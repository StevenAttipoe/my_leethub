class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return n
        if n == 1 or n == 2:
            return 1

        a, b, c = 0, 1, 1

        for i in range(3, n + 1):
            d = a + b + c
            a, b, c = b, c, d

        return c

    def tribonacci2(self, n: int) -> int:
        if n == 0:
            return n
        if n == 1 or n == 2:
            return 1

        dp = [0] * (n + 1)
        dp[1] = dp[2] = 1

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

        return dp[-1]
        