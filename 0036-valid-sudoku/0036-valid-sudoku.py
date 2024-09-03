class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = set()
        cols = set()
        boxes = set()

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                
                val = board[i][j]

                if ((i, val) in rows or
                    (j, val) in cols or
                    (i // 3, j // 3, val) in boxes
                ) : return False

                rows.add((i, val))
                cols.add((j, val))
                boxes.add((i // 3, j // 3, val))

        return True