class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        maxlength = 0
        memo = {}

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == '1':
                    length = self.recurseSquaresMemo(matrix, i, j, memo)
                    maxlength = max(maxlength, length)

        return maxlength * maxlength

    def recurseSquaresMemo(self, matrix, i, j, memo):
        if i == len(matrix) or j == len(matrix[0]):
            return 0

        if (i, j) in memo:
            return memo[(i, j)]

        right = self.recurseSquaresMemo(matrix, i, j + 1, memo)
        bottom = self.recurseSquaresMemo(matrix, i + 1, j, memo)
        diagonal = self.recurseSquaresMemo(matrix, i + 1, j + 1, memo)

        res = 1 + min(right, bottom, diagonal) if matrix[i][j] == '1' else 0
        memo[(i, j)] = res
        return memo[(i, j)]

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
        