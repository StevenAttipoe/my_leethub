class Solution:
    """
        Time - O(n * m)
        Space - O(n * m)
    """
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        memo = {}

        def helper(i, j):
            if i >= len(matrix) or j >= len(matrix[0]):
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            right = helper(i, j + 1)
            down = helper(i + 1, j)
            diag = helper(i + 1, j + 1)

            memo[(i, j)] = 0
            if matrix[i][j] == '1':
                memo[(i, j)] = 1 + min(right, down, diag)

            return memo[(i, j)]

        helper(0, 0)
        return (max(memo.values())) ** 2



    # Time - O(n * m)^ 2
    def maximalSquare2(self, matrix: List[List[str]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        maxlength = 0

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == '1':
                    length = self.recurseSquares(matrix, i, j)
                    maxlength = max(maxlength, length)

        return maxlength * maxlength

    def recurseSquares(self, matrix, i, j):
        if i == len(matrix) or j == len(matrix[0]):
            return 0

        right = self.recurseSquares(matrix, i, j + 1)
        bottom = self.recurseSquares(matrix, i + 1, j)
        diagonal = self.recurseSquares(matrix, i + 1, j + 1)

        return 1 + min(right, bottom, diagonal) if matrix[i][j] == '1' else 0
        