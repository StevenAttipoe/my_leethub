class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
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