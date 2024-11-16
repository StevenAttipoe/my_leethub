class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        
        moves = [
            [4, 6],
            [6, 8],
            [7, 9],
            [4, 8],
            [3, 9, 0],
            [],
            [1, 7, 0],
            [2, 6],
            [1, 3],
            [2, 4]
        ]

        mod =  10 ** 9 + 7
        dp = [1] * 10
       
        for _ in range(n - 1):
            next_dp = [0] * 10
            for i in range(10):
                for m in moves[i]:
                    next_dp[m] += dp[i]
            dp = next_dp
        
        return sum(dp) % mod
        