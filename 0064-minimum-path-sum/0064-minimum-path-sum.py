class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        memo = [[0 for _ in range(COLS)] for _ in range(ROWS)]

        def dfs(i, j):
            if i == ROWS - 1 and j == COLS - 1:
                return grid[i][j]

            if memo[i][j] != 0:
                return memo[i][j]

            if i == ROWS - 1:
                return grid[i][j] + dfs(i, j + 1)

            if j == COLS - 1:
                return grid[i][j] + dfs(i + 1, j)

            memo[i][j] = grid[i][j] + min(dfs(i + 1, j), dfs(i, j + 1))

            return memo[i][j]

        return dfs(0, 0)


    