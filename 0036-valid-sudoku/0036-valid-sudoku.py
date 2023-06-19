class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = set()
        cols = set()
        matrix = set()
        
        for r in range(9):
            for c in range(9):

                if board[r][c] == '.':
                    continue

                if ((r, board[r][c]) in rows or
                    (c, board[r][c]) in cols or
                    (r // 3, c //3, board[r][c]) in matrix):
                    return False

                rows.add((r, board[r][c]))
                cols.add((c, board[r][c]))
                matrix.add((r // 3, c // 3, board[r][c]))

        return True

