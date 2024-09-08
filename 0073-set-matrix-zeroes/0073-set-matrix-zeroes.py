class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
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

        