class Solution:
    """
    Bottom-up dp
    Time - O(n * m)
    Space - O(n)
    """
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        ROWS, COLS = len(matrix), len(matrix[0])
        dp = [0] * (COLS + 1)
        maxlength, prev = 0, 0

        for i in range(1, ROWS + 1):
            for j in range(1, COLS + 1):
                temp = dp[j]
                if matrix[i - 1][j - 1] == "1":
                    dp[j] = 1 + min(dp[j], min(dp[j - 1], prev))
                    maxlength = max(maxlength, dp[j])
                else:
                    dp[j] = 0
                prev = temp
        return maxlength * maxlength

    """
        Bottom-up dp
        Time - O(n * m)
        Space - O(n * m)
    """

    def maximalSquare2(self, matrix: List[List[str]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        maxlength = 0

        for i in range(1, ROWS + 1):
            for j in range(1, COLS + 1):
                if matrix[i - 1][j - 1] == "1":
                    dp[i][j] = 1 + min(
                        dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]
                    )
                    maxlength = max(maxlength, dp[i][j])
        return maxlength * maxlength

    """
        Top bottom recursive memoization
        Time - O(n * m)
        Space - O(n * m)
    """

    def maximalSquare3(self, matrix: List[List[str]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        memo = {}

        def helper(i, j):
            if i >= len(matrix) or j >= len(matrix[0]):
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            down = helper(i + 1, j)
            right = helper(i, j + 1)
            diag = helper(i + 1, j + 1)

            memo[(i, j)] = 0
            if matrix[i][j] == "1":
                memo[(i, j)] = 1 + min(right, down, diag)

            return memo[(i, j)]

        helper(0, 0)
        return (max(memo.values())) ** 2

    # Time - O(n * m)^ 2
    def maximalSquare4(self, matrix: List[List[str]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        maxlength = 0

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == "1":
                    length = self.recurseSquares(matrix, i, j)
                    maxlength = max(maxlength, length)

        return maxlength * maxlength

    def recurseSquares(self, matrix, i, j):
        if i == len(matrix) or j == len(matrix[0]):
            return 0

        right = self.recurseSquares(matrix, i, j + 1)
        bottom = self.recurseSquares(matrix, i + 1, j)
        diagonal = self.recurseSquares(matrix, i + 1, j + 1)

        return 1 + min(right, bottom, diagonal) if matrix[i][j] == "1" else 0
