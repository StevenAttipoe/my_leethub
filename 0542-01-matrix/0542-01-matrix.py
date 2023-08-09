class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(mat), len(mat[0])

        for i in range(ROW):
            for j in range(COL):
                if mat[i][j] > 0:
                    top = mat[i - 1][j] if i > 0 else math.inf
                    left = mat[i][j - 1] if j > 0 else math.inf
                    mat[i][j] = min(top, left) + 1

        for i in range(ROW - 1, -1, -1):
            for j in range(COL - 1, -1, -1):
                if mat[i][j] > 0:
                    right = mat[i][j + 1] if j < COL - 1 else math.inf
                    bottom = mat[i + 1][j] if i < ROW - 1 else math.inf
                    mat[i][j] = min(mat[i][j], bottom + 1, right + 1) 

        return mat
        
    def updateMatrix2(self, mat: List[List[int]]) -> List[List[int]]:
        queue = []
        neighbours = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = '*'

        for r, c in queue:
            for nr, nc in neighbours:
                row = r + nr
                col = c + nc
                if 0 <= row < len(mat) and 0 <= col < len(mat[0]) and mat[row][col] == '*':
                    mat[row][col] = mat[r][c] + 1
                    queue.append((row, col))
        return mat