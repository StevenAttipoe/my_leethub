class Solution:
    # O(M * N) time and O(1) space
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False

        # Determine which rows/cols to set to zero
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0

                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        # Set rows/cols to zero
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # Set first col to zero if needed
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
        
        # Set first row to zero if needed
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0

    # O(M * N) time and O(M + N) space
    def setZeroes2(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        rowSet, colSet = set(), set()

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    rowSet.add(i)
                    colSet.add(j)

        for i in range(ROWS):
            for j in range(COLS):
                if i in rowSet or j in colSet:
                    matrix[i][j] = 0
        


    # O(M * N) time and O(M * N) space
    def setZeroes3(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.ROWS, self.COLS = len(matrix), len(matrix[0])
        copy = [[0 for i in range(self.COLS)] for j in range(self.ROWS)]

        for i in range(self.ROWS):
            for j in range(self.COLS):
                copy[i][j] = matrix[i][j]

        
        for i in range(self.ROWS):
            for j in range(self.COLS):
                if copy[i][j] == 0:
                    self.dfs(i, j, matrix)

    def dfs(self, i, j, matrix):
        p = i
        while p >= 0:
            matrix[p][j] = 0
            p -= 1

        p = i
        while p < self.ROWS:
            matrix[p][j] = 0
            p += 1
        
        p = j
        while p >= 0:
            matrix[i][p] = 0
            p -= 1

        p = j
        while p < self.COLS:
            matrix[i][p] = 0
            p += 1

        