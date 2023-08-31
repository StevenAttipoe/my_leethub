class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS, COLS = m, n

        paths_dp = [[1 for i in range(COLS)] for i in range(ROWS)]

        for i in range(1, ROWS):
            for j in range(1, COLS):
                paths_dp[i][j] = paths_dp[i][j - 1] + paths_dp[i - 1][j]

        return paths_dp[-1][-1]
        